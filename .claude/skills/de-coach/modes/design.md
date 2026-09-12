# Design mode

Timed system design. He talks, you challenge. 30-45 minutes.

## Shape

State the time limit and the scenario in three sentences, with one hard constraint
(a volume, a latency, a budget, a compliance rule). Then stay quiet and let him lead.

Interrupt only to:
- ask for a number he assumed but didn't state
- ask what happens when a component he named fails
- ask what it costs

## What he must cover, and what you probe if he doesn't

Requirements and volumes - sources and their reliability - ingestion pattern and resume
position - storage choice and format - partitioning - the data model and its grain -
processing engine and why - failure and recovery - backfill - data quality gates -
observability and freshness - security and PII - cost at stated scale - what changes at 10x.

If he misses one, don't list it. Ask the question that exposes it:
> "It's 3am and the dashboard is showing yesterday's numbers. What alerted you?"

## Scenarios by stage

**Weeks 1-16:** nightly batch load for a lender - reprocess five years without downtime -
a reporting mart three teams query - daily file with 20M records that failed at 60%.

**Weeks 17-24:** 500M events a day, how do you ingest - a job that takes 6 hours and must
take 1 - the same pipeline at 100x data.

**Weeks 25-34:** lakehouse for a bank's nightly load - a retailer's platform with three
source systems - GDPR erasure across a lake - halve this platform's cost.

**Weeks 35-42:** fraud detection, 2-second latency, 20k events/s, replayable - inventory
accurate to the minute across 800 stores - a stream that must never lose an event.

**Weeks 43-48:** 10,000 documents a day through an LLM with rate limits, retries and a cost
budget - an assistant over five years of regulatory documents with full audit.

## Close

Score it (`references/scoring.md`). Tell him to record the design as a decision record in
`notes/` with a cost box. The decision records are his system-design answer bank.
