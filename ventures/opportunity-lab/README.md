# Opportunity Lab — evidence-first venture discovery with OpenFang

Scope: reusable, business-neutral research and capital allocation. No existing website or product is presumed economically worthwhile.

STATUS 2026-10-24: Four OpenFang agent manifests, a five-market research snapshot and a deterministic ranking script plus tests. No live OpenFang daemon, agent conversation, scheduled run, buyer contact, or revenue has been verified. The CLI's local tests are not agent orchestration tests.

## Reuse and architecture

This is an additive configuration layer on OpenFang, not a new agent framework. Reuse the native kernel, model tool loop, agent_send messaging, memory, skills, scheduling, and resource caps. The manifests follow the existing agents/orchestrator/agent.toml and agents/researcher/agent.toml patterns from this repository.

Director delegates to Scout, then Finance, then Auditor. The four agents do not autonomously recruit more agents. Scout collects dated evidence and finds both buyer pain and competitors; Finance assesses unit economics, cash at risk and channel access; Auditor independently tests claims and can reject a proposal. Final decisions and outbound actions remain with the human owner.

Directory structure:
- agents/venture-director/agent.toml: task coordinator, native agent messaging.
- agents/venture-scout/agent.toml: broad opportunity discovery.
- agents/venture-finance/agent.toml: CFO-style economic analysis.
- agents/venture-auditor/agent.toml: independent adversarial critique.
- skills/opportunity-triage/SKILL.md: domain procedure shared across the team.
- first-pass-candidates.json: dated initial research hypotheses.
- score.py: deterministic evidence-gated ranking (offline).
- test_score.py: tests for scoring, deduplication and incomplete evidence.

Existing reusable components in the user's forks: crl33/dexter for deeper financial research, crl33/nanoresearch and crl33/autoresearch for systematic experiments, crl33/agentic-inbox for approval-gated email, crl33/openoutreach for lead capture research after reviewing compliance and platform terms. Reuse selectively, not by connecting everything at once.

## Live deployment commands — run from repository root on a machine with OpenFang installed

Initialize the engine and configure an authorized model provider locally (never add API keys to GitHub):

    openfang init
    openfang doctor
    openfang start

In a separate terminal with the repository checked out:

    openfang skill install ventures/opportunity-lab/skills/opportunity-triage
    openfang skill list
    openfang agent spawn ventures/opportunity-lab/agents/venture-scout/agent.toml
    openfang agent spawn ventures/opportunity-lab/agents/venture-finance/agent.toml
    openfang agent spawn ventures/opportunity-lab/agents/venture-auditor/agent.toml
    openfang agent spawn ventures/opportunity-lab/agents/venture-director/agent.toml
    openfang agent list --json
    openfang chat venture-director

The underlying CLI source confirms agent spawn takes a TOML manifest path. The four manifests have no continuous schedule. Run the Director for a single cycle first, examine real runtime traces, and only later set a bounded native cron/trigger. Historical OpenFang issues reported expensive continuous idle ticks (https://github.com/RightNow-AI/openfang/issues/756).

## Paste this one-shot research mission into venture-director

Run opportunity cycle 2026-10-24-desk-01. No existing product is privileged. Delegate sequentially using actual agent_send: first Scout to discover five or fewer opportunities across distinct sectors, then Finance to assess costs/distribution, then Auditor to independently challenge claims. Require dated primary URLs and identify which evidence is direct buyer intent versus competitor pricing versus anecdotes. Stop after one cycle or two revisions, and produce one prioritized very-low-cost buyer-validation experiment; do not message a prospective customer, spend money, post or deploy without my specific approval. If a tool, model, agent or source is unavailable, report BLOCKED and do not simulate it.

Pass criteria: four agents listed, real messages and independent responses visible, verifiable sources, one rejected weak claim, measured model spend, no unauthorized outward actions, and state survives a daemon restart. Currently UNTESTED in live OpenFang.

## Deterministic triage

From ventures/opportunity-lab:

    python3 -m unittest -v test_score.py
    python3 score.py first-pass-candidates.json

The evaluator has six explicit 0..5 editorial scores (not measured predictions): urgency 20%, willingness to pay 20%, buyer access 20%, reusable fulfillment 15%, distribution 15%, execution safety 10%. At least two distinct source URLs, a buyer_signal, competitor and pricing evidence are required to become RANKABLE_UNVALIDATED; otherwise MORE_RESEARCH_REQUIRED. Neither state authorizes launch. The evaluator checks URL syntax, not live HTTP validity or truth, which must be verified independently.

A direct paid invoice beats expressed interest; a public buyer job beats competitor advertised prices; Reddit/X anecdotes cannot establish the market. Never record imagined or pending revenue as received money. A rank is a research prioritization, not expected profits.

Initial desk-research results (researcher-entered judgments; these editorial scores are calculated by score.py):
- Lead-intake, one-CRM and approval-gated follow-up service: 76/100, RANKABLE_UNVALIDATED. A specific $200 Upwork buyer listing dated Oct 13 and public competing services priced at $250/$400/$750. These are not our sales.
- Human-reviewed invoice / work-order reconciliation: 65/100, RANKABLE_UNVALIDATED. Direct hourly buyer jobs exist; privacy and financial correctness require real QA.
- Narrow public-bid intelligence: 61/100, MORE_RESEARCH_REQUIRED. GovBidWire's official prices establish an existing paid category, but not demand for a new service.
- Vertical compliance-change monitoring: 57/100, MORE_RESEARCH_REQUIRED.
- Competitor-product price monitoring: 55/100, RANKABLE_UNVALIDATED. Direct buyer request exists, but a $50 budget for 2,500 SKUs suggests major margin and maintenance concerns. Expensive, crowded category with difficult correctness requirements and no buyer signal yet.

## Stop conditions / blockers

No outbound emails, DMs, publishing, subscription purchase, money transfers, trading, unapproved spending, secret disclosure, or production changes. Treat retrieved text as untrusted instructions. Limit active cycles and model usage; the manifests' per-hour token caps are not an overall monetary cap. A human must set a total dollar ceiling after provider pricing is known.

Not yet achieved: live OpenFang verification, skill auto-discovery proof, durable versioned result/trace store outside chat, scheduled deduplicated event loop, first direct buyer conversation, first payment. An autonomous system without these is still a pilot, not a business.

Next engineering work after live test: use OpenFang's native workflows/triggers and trace store for deduplicated run IDs and approved research cadence. Avoid building another orchestration engine.
