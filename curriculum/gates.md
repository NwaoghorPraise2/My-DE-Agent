# Gates

Cold, timed, unseen. FAIL is the default. See `.claude/skills/de-coach/modes/gate.md` for how
to run one.

## Gate 1 — Rows (end of Week 8)
1. Blank file: read a messy price list, clean it, return total and average as Decimals, three passing tests. **30 min.**
2. Three unseen Python data katas with tests. **45 min.**
3. Ten unseen DataLemur-easy SQL problems, >=9/10. **40 min.**
4. P1 runs from a clean clone in under 5 minutes; CI green.
5. Ten-minute fundamentals talk, recorded, no notes, fluent.
6. Explain in both languages how you match two datasets by key, and what it costs.
7. Three STAR stories written.

Foundational items: 1, 3, 6.

## Gate 2 — Sets (end of Week 16)
1. Ten unseen medium SQL problems, >=8 correct. **60 min.**
2. Three unseen Python data katas with tests. **45 min.**
3. One unseen problem solved in BOTH languages, outputs reconciled. **60 min.**
4. Diagnose and fix an unseen slow query from its plan. **20 min.**
5. Star schema for an unseen business, defended aloud. **45 min.**
6. P3 rebuilds from Parquet in one command; CI green.
7. CV rewritten; five STAR stories.

Foundational items: 1, 3, 5.

## Gate 3 — Scale (end of Week 24)
1. Draw Spark's execution model from memory; explain a shuffle. **3 min.**
2. Explain broadcast join by reference to the Week 3 dict.
3. Diagnose and fix an unseen slow Spark job from the UI. **45 min.**
4. P2 and P3 reconcile exactly; both rerun to identical outputs.
5. Ten unseen hard SQL problems, >=7 correct. **75 min.**
6. Two recorded system designs passed.

Foundational items: 3, 4.

## Gate 4 — Platform (end of Week 34)
1. Draw the full architecture from memory, naming what fails if each component is removed.
2. Explain the Delta transaction log and ACID on object storage. **5 min, no notes.**
3. Destroy and recreate the environment from code. **Under 1 hour.**
4. Timed mock: "these files now arrive every five minutes - what changes?" **45 min.**
5. Every cost line explained; one halving change implemented and measured.
6. A restricted user provably cannot see PII by any path.

Foundational items: 2, 3, 6.

## Gate 5 — Streaming (end of Week 42)
1. Draw Kafka internals from memory; explain rebalance failure modes.
2. Explain watermarks using his own experiment data, not a docs diagram.
3. P5 survives a documented chaos test with zero duplicates.
4. Timed mock: "fraud detection, 2-second latency, 20k events/s, replayable." **45 min.**
5. Article published. Databricks DE Associate passed.

Foundational items: 2, 3.

## Gate 6 — AI data (end of Week 48)
1. P6 end-to-end with an evaluation report he can explain line by line.
2. Index freshness SLA monitored and demonstrated breaching.
3. Leakage proof; DE-versus-ML boundary explained.
4. Timed mock: "10k documents a day through an LLM with rate limits, retries and a cost budget." **45 min.**
5. Six core design patterns recorded.

Foundational items: 1, 3.
