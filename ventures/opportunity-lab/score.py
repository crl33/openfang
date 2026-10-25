#!/usr/bin/env python3
"""Offline, deterministic ranking of researched opportunities. No LLM or network use."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

WEIGHTS = {
    "pain_urgency": 0.20,
    "willingness_to_pay": 0.20,
    "buyer_access": 0.20,
    "reuse_feasibility": 0.15,
    "distribution": 0.15,
    "execution_safety": 0.10,
}
REQUIRED_FIELDS = ("id", "name", "buyer", "problem", "evidence", "scores")


def rank(candidates):
    if not isinstance(candidates, list):
        raise ValueError("Expected a JSON array of candidates")
    result, seen = [], set()
    for c in candidates:
        if not isinstance(c, dict):
            raise ValueError("Each candidate must be an object")
        missing = [key for key in REQUIRED_FIELDS if key not in c]
        if missing:
            raise ValueError(f"Missing fields: {missing}")
        candidate_id = c["id"]
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            raise ValueError("Candidate id must be a nonempty string")
        if candidate_id in seen:
            raise ValueError(f"Duplicate candidate id: {candidate_id}")
        seen.add(candidate_id)
        for key in ("name", "buyer", "problem"):
            if not isinstance(c[key], str) or not c[key].strip():
                raise ValueError(f"{candidate_id}: nonempty {key} required")
        if not isinstance(c["scores"], dict) or set(c["scores"]) != set(WEIGHTS):
            raise ValueError(f"{candidate_id}: all and only six scoring dimensions required")
        if not all(type(c["scores"][k]) in (int, float) and 0 <= c["scores"][k] <= 5 for k in WEIGHTS):
            raise ValueError(f"{candidate_id}: scores must be numbers in range 0..5 (no bool)")
        if not isinstance(c["evidence"], list):
            raise ValueError(f"{candidate_id}: evidence must be a list")
        unique_sources, source_types = set(), set()
        for ev in c["evidence"]:
            if not isinstance(ev, dict) or not all(isinstance(ev.get(k), str) and ev[k].strip() for k in ("url", "date", "type", "note")):
                raise ValueError(f"{candidate_id}: evidence requires nonempty url/date/type/note")
            u = urlparse(ev["url"])
            if u.scheme != "https" or not u.hostname:
                raise ValueError(f"{candidate_id}: evidence URL must be HTTPS")
            unique_sources.add(ev["url"].split("#")[0])
            source_types.add(ev["type"])
        score = round(sum(c["scores"][k] * w for k, w in WEIGHTS.items()) * 20, 1)
        checks = {
            "two_distinct_sources": len(unique_sources) >= 2,
            "buyer_demand_signal": "buyer_signal" in source_types,
            "known_competitor": "competitor" in source_types,
            "pricing_evidence": "pricing" in source_types,
        }
        # A research rank is not authorization to build or claim paying customers.
        status = "RANKABLE_UNVALIDATED" if all(checks.values()) else "MORE_RESEARCH_REQUIRED"
        result.append({"id": candidate_id, "name": c["name"], "score": score,
                       "status": status, "gates": checks,
                       "buyer_validation": "NOT_RUN", "verified_revenue_usd": None})
    return sorted(result, key=lambda x: (-x["score"], x["id"]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON candidate array")
    args = p.parse_args()
    print(json.dumps(rank(json.loads(args.input.read_text(encoding="utf-8"))), indent=2))


if __name__ == "__main__":
    main()
