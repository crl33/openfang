---
name: opportunity-triage
description: Research, audit, and prioritize commercially plausible opportunities using dated evidence, skeptical unit economics, and rapid buyer-validation experiments; never conflate competitor pricing with our sales.
---

# Opportunity Triage Skill

Use when the user or venture-director asks for new commercial ideas, profit pathways, market demand, opportunity scores, business validation, or go/no-go prioritization. This is a research procedure, not an authorization to act externally.

## Operating sequence

1. **Discover, don't preselect.** Look across at least three unrelated sectors, including unglamorous manual work that buyers already budget for. Use public buyer requests, paid substitutes, complaints with evidence, and time-consuming workflows. Maintain an explicit unexamined-opportunities backlog.
2. **Ground in dated sources.** Search authoritative/publicly available sources, fetch originals, identify the exact buyer, problem, alternative, current procurement channel and potential contract cadence. Every candidate must have distinct dated URLs. Treat X/Reddit posts as leads, not audited revenue.
3. **Seek negative evidence.** Investigate saturated markets, high buyer-acquisition costs, low gross margins, regulatory/compliance barriers, expensive integrations, data quality, licensing, prohibitions on scraping and poor distribution.
4. **Reuse-first engineering.** Before proposing new code, check GitHub and existing user-owned forks for maintained code or tooling that already solves 80% of delivery. Record exact repository, license, recency, maintainer health, operating requirements, security considerations and integration boundaries. Do not install untrusted repositories without review.
5. **Economic test.** Determine target price as a hypothesis, unit cost range (model tokens, API data, infrastructure, payment fees, QA time, support), acquisition channel, realistic customer count, effective gross margin, expected time to cash and payback. Unknown inputs must remain UNKNOWN; do not manufacture CLV/CAC.
6. **Independent challenge.** Auditor must revisit sources and reject at least one weak assumption. Identify the cheapest authorized test that would make the recommendation fail.
7. **Only then recommend action.** Allowed next states: STOP, INVESTIGATE, VALIDATE_WITH_BUYERS, BUILD_AFTER_APPROVAL. The last state is not granted by a ranking score alone.

## Handoff contract

Include task_id, run_id, owner, next_owner, date/time, candidate_id, buyer, painful manual workflow, source_urls with last observation date and note, direct-demand status, current paid alternatives, reused-code options, risks, costs (known versus guessed), adverse case, experiment, stop condition and specific human approvals required.

Use ventures/opportunity-lab/first-pass-candidates.json as an example schema only; do not treat the three seeded ideas as mandatory. After editing candidate JSON, run the deterministic Python scorer. Rank results are editorial and cannot evidence revenue.

## Reliability policy

When a source is missing, unverifiable, stale or restricted, downgrade confidence and disclose it. Preserve evidence provenance. Do not invent buyer conversations, scraped metrics, ROI, gross revenue, payment confirmations or deployed deliverables. Uncertainty is a valid research result.

## Spending and external-action safety

Never automatically email, DM, post, sign up, make purchases, accept terms, process payments, deploy, merge, or touch production. Such actions require explicit user approval scoped to recipient/action/amount. Do not perform protected-platform scraping. Respect licensing, copyrights, privacy and anti-spam requirements.

Stop after one bounded cycle or two revisions. Do not generate endless agent-to-agent discussion, duplicate tasks, or hourly idle loops. Use OpenFang-native memory, role permissions, schedules and budget tooling instead of creating parallel orchestration infrastructure.

## Acceptance

One actually completed Director→Scout→Finance→Auditor handoff chain with traceable tool invocations, working source URLs, independent rejection of a weak claim, and a decision with one falsifiable low-cost test. A manifest file and a simulated message are not sufficient.
