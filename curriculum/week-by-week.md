# Curriculum — week by week

19 h/week. Python and SQL run in parallel from Week 1, paired so each week's two topics are
the same underlying idea seen twice. Spark arrives Week 17, once both are fluent.

**The project spine.** Northbank Credit, a UK consumer lender, 400k loan accounts repaid by
Direct Debit. Daily collection files out; returns and mandate-change files back; arrears aged
and retried. P1 (Python engine) → P3 (Postgres mart) → P2 (Spark history) → P4 (lakehouse) →
P5 (retail streaming) → P6 (legal document intelligence).

**Weekly rhythm.** Mon SQL learn+drill 2h · Tue Python learn+kata 2h · Wed build 3h + break-and-fix 0.5h ·
Thu drill 0.75h + build 1.75h + design 1h · Fri read 1h + tools 0.5h + PR 0.5h ·
Sat bridge challenge 3h · Sun review 1h + interview prep 1h + applications 1h.

---

## Stage 1 — Rows and values (Weeks 1–8)

### Week 1 — Types, twice
- **Python:** int/float/str/bool/None; `Decimal` for money (run `0.1+0.2`); string methods for parsing — slicing, strip, split, join, zfill, startswith, case; truthiness; f-strings; explicit casting and casting that fails; UTF-8 vs Latin-1.
- **SQL:** Postgres 16 in Docker; psql; CREATE TABLE; NUMERIC vs FLOAT vs INT, TEXT, DATE, TIMESTAMPTZ, BOOLEAN; INSERT; first SELECT.
- **Idea:** A type system is a promise about what a value can hold. He makes it twice — parser and table — and a disagreement silently corrupts data at the boundary.
- **Build:** Parse one 106-char fixed-width BACS record into a typed dict. Create the `collection_attempt` table with matching types. Insert one row by hand.
- **Practise:** 15 Python functions with tests (parse_price, is_palindrome, word_frequency, chunk_list, running_total). SQLBolt 1–6.
- **Prove:** Parse ten records, insert them, prove with SQL that no amount lost precision. 30 min.

### Week 2 — Filtering: imperative and declarative
- **Python:** if/elif/else; `match` and dict dispatch; for vs while; break/continue/loop-else; range, enumerate, zip; nested loops and where they turn quadratic; comprehensions and when one is worse than a loop.
- **SQL:** WHERE, ORDER BY, LIMIT, DISTINCT, aliases, CASE, COALESCE, casting, BETWEEN, IN, LIKE; basic string and date functions.
- **Idea:** The same predicate two ways. Python says how to find rows; SQL says which rows and something else decides how. This mental shift is what makes Spark easy in Week 17.
- **Build:** Parse a whole submission file — header, records, trailer. Classify by transaction code. Modulus-check sort codes and account numbers. Verify trailer count and total. Load to Postgres; answer five questions in both languages.
- **Practise:** 20 control-flow katas. SQLBolt 7–12. 10 DataLemur easy.
- **Prove:** Five questions, two answers each, identical.

### Week 3 — The join, by hand and by the planner
- **Python:** lists, tuples, sets, dicts as the hash map — lookup, grouping, counting, nesting, defaultdict, Counter, get vs [] vs setdefault; when a list of dicts should be a dict of lists; Big-O as instinct.
- **SQL:** PK/FK and constraints; INNER, LEFT, RIGHT, FULL, CROSS, self-joins; semi and anti joins with EXISTS/NOT EXISTS; NOT IN with nullable columns; the LEFT JOIN + WHERE trap; fan-out.
- **Idea:** A join is a hash table. He builds one by hand, then watches Postgres build the same thing. Returns as broadcast join (W19) and as a plan node (W14).
- **Build:** Match collections to mandates via a Python dict; write the identical SQL join; reconcile row for row. Rewrite as a nested loop, time both on 500k records, record the numbers.
- **Practise:** 20 data katas (dedupe preserving order, group by customer, top-5 with heap, two-sum, merge sorted lists, first duplicate, running max, sliding-window average, hash join by hand, flatten nested JSON, find gaps in IDs, chunk an iterator). 25 SQL join problems.
- **Prove:** 3 unseen katas in 45 min. 10 DataLemur easy joins, ≥9/10 in 40 min. Explain the LEFT JOIN + WHERE trap with a query.

### Week 4 — Time, in code and in the calendar table
- **Python:** functions — params, defaults, the mutable-default trap, scope, docstrings, type hints; pure vs impure functions; Decimal quantising and rounding modes; datetime, date, timedelta, zoneinfo, ISO-8601, UTC discipline, epoch.
- **SQL:** EXTRACT, DATE_TRUNC, intervals, date arithmetic, AGE, formatting; TIMESTAMPTZ vs TIMESTAMP; `generate_series` and the date spine.
- **Idea:** A working day is business logic, not a data type. Decide once whether it lives in code or a table — computing it in both guarantees drift.
- **Build:** Working-day due-date calendar in Python (weekends, bank holidays, 3-working-day advance notice). Then `dim_date` in Postgres from a spine. Assert they agree for 1,826 days.
- **Practise:** 12 Python date katas. 15 SQL date problems. 10 DataLemur easy.
- **Prove:** Both agree across five years. Parametrised tests pass for payment day 31 in February, Good Friday, the Christmas cluster.

### Week 5 — Bulk movement, and running twice safely
- **Python:** open, `with`, pathlib; line-by-line vs whole-file; generators and `yield`; csv and its dialect traps; json; Parquet via pyarrow — columnar layout, explicit schemas, compression; atomic writes.
- **SQL:** BEGIN/COMMIT/ROLLBACK; UPSERT with INSERT … ON CONFLICT; COPY vs row-by-row INSERT; sequences and identity; truncate vs delete.
- **Idea:** Idempotency. A generator streams data in without holding it; a transaction plus UPSERT lets the same data arrive twice without damage.
- **Build:** Three readers behind one interface. Parquet writer with declared schema under `date=YYYY-MM-DD/`. COPY loader with idempotent upsert. Load the same day twice, prove counts unchanged.
- **Practise:** 10 file katas including a 1 GB stream with flat memory. 15 SQL transaction/upsert problems. Measure COPY vs inserts.
- **Prove:** Load a day, load it again, identical counts and checksums.

### Week 6 — Collapsing many rows into one
- **Python:** grouping and counting with dict, defaultdict, Counter; sorting — stable, multi-key, sort vs sorted; heapq for top-N; deque and stacks; itertools.groupby and its gotcha.
- **SQL:** GROUP BY, HAVING vs WHERE; COUNT(*) vs COUNT(col) vs COUNT(DISTINCT); SUM/AVG/MIN/MAX; FILTER; GROUPING SETS and ROLLUP.
- **Idea:** Aggregation is one idea with two costs. Python holds groups in memory; the planner may sort or hash and may spill. Same answer, different failure mode at scale.
- **Build:** Daily collections summary computed in Python from the parsed file and in SQL from the table. Reconcile to the penny. Add the rollup version.
- **Practise:** 15 grouping/top-N katas. 20 SQL aggregation problems. 10 DataLemur medium.
- **Prove:** Both summaries agree exactly. Explain which he'd keep in production and why.

### Week 7 — Where bad data gets stopped
- **Python:** try/except/else/finally; catching narrowly; re-raising; custom exceptions carrying context; record-level vs run-level failure; the logging module, structured JSON logs, a correlation ID per run; at-least-once / exactly-once / at-most-once.
- **SQL:** NOT NULL, UNIQUE, CHECK, FOREIGN KEY; referential integrity and orphan detection; NULL and three-valued logic; deferred constraints.
- **Idea:** Every validation rule can live in the parser, the table, or neither. Constraints are guarantees you can't forget; code checks are guarantees you can explain to a user.
- **Build:** Quarantine to `/data/rejected/` with reasons. Structured logs under one run ID. Run summary. Then add the DB constraints that would have caught the same problems; document which rule lives where.
- **Practise:** 8 error-handling katas. 15 SQL constraint/NULL problems. Break-and-fix runs a full hour.
- **Prove:** Feed a poisoned file. Nothing crashes, nothing bad lands, the reject report explains every row.

### Week 8 — Sources, tooling, P1 complete
- **Python:** sources — files, HTTP APIs (httpx, pagination, rate limits, timeouts, retries with backoff), databases, Kafka's model conceptually; full vs incremental and the watermark; pydantic at the boundary; config and secrets; pytest fixtures, parametrize, mocking HTTP, coverage.
- **SQL:** views; subqueries — scalar, correlated, derived; first look at CTEs; psycopg and parameterised queries.
- **Idea:** A source is anything you can ask for records and resume from. File offset, API cursor, DB watermark, Kafka offset — four names for one concept.
- **Build:** P1 complete. `Source` abstraction with file and API implementations; GOV.UK bank holidays API with retry, timeout, cached fallback. Containerised. 25+ tests, coverage ≥90%, CI green. Tag v1.0.0.
- **Tools:** Linux drill 20 min timed. 1 GB log, 10 shell one-liners. Git branch/PR/conflict/squash/tag. Docker multi-stage.
- **GATE 1** — see `gates.md`.

---

## Stage 2 — Sets, windows, models (Weeks 9–16)

### Week 9 — Latest per key
- **Python:** comprehensions in depth; itertools (groupby, islice, chain, tee, pairwise); generator pipelines; functools (reduce, lru_cache, partial); "keep newest per key" three ways.
- **SQL:** windows I — OVER, PARTITION BY, ORDER BY; ROW_NUMBER, RANK, DENSE_RANK and ties; percent of total; the dedupe pattern.
- **Idea:** A window function is a group-by that doesn't collapse rows. Sort within a partition, then number.
- **Build:** Latest mandate state per account, Python dict and SQL ROW_NUMBER, reconciled. Dedupe a double-loaded day both ways.
- **Prove:** Explain RANK vs DENSE_RANK vs ROW_NUMBER with ties, aloud, query on screen.

### Week 10 — Comparing a row to its neighbour
- **Python:** pairwise iteration, sliding windows, running accumulators, state across a sorted sequence.
- **SQL:** LAG/LEAD; running totals and moving averages with ROWS vs RANGE frames; NTILE, FIRST_VALUE, LAST_VALUE; cumulative distinct.
- **Idea:** Ordering makes new facts available. The gap between two rows is data in neither one.
- **Build:** Link each failed collection to its re-presentation with LAG; retry effectiveness by reason code; running collected-to-date. Same linkage in Python, reconciled.
- **Prove:** 10 DataLemur mediums, ≥7/10 in 60 min.

### Week 11 — Streaks and recursion
- **Python:** recursion vs iteration; state machines as explicit code; walking a parent-child hierarchy; cycle detection.
- **SQL:** CTEs, chained CTEs; recursive CTEs; gaps and islands; sessionisation with LAG; UNION/UNION ALL/INTERSECT/EXCEPT; refactoring a 120-line query into six CTEs.
- **Idea:** Consecutive-run problems look different in each language and are the same problem.
- **Build:** Consecutive-missed-payment streaks — the arrears stage calculation — as a Python state machine and a gaps-and-islands query. Reconcile across 400k accounts.
- **Prove:** Both agree on every account; disagreements written down.

### Week 12 — Two kinds of model
- **Python:** classes, `__init__`, dataclasses, pydantic models; modules and packages; modelling the domain in objects.
- **SQL:** grain; fact types (transaction, periodic snapshot, accumulating snapshot); conformed/junk/degenerate/role-playing dims; star vs snowflake; surrogate keys; SCD 1/2/3; late-arriving dims; 1NF–3NF and deliberate denormalisation.
- **Idea:** Application model and analytical model differ on purpose. One optimises a single account's correctness; the other a million accounts' comparison.
- **Build:** Domain objects in pydantic. Remodel the mart as a star: collection lifecycle as accumulating-snapshot fact, mandates SCD2, date dim from W4. Write the mapping.
- **Prove:** Defend the grain on a whiteboard, ten minutes, no notes. Star schema for an unseen business in 45 min.

### Week 13 — Where the transformation runs
- **Python:** pandas essentials and Polars equivalents; when a dataframe library beats loops and when it costs memory; mypy, ruff, black.
- **SQL:** views vs materialised views and the refresh question; ETL vs ELT; transform-in-database.
- **Idea:** The same transformation can run in three places, and the choice is cost, testability and readership — not speed.
- **Build:** Five reports as views; materialise the daily arrears snapshot with a refresh policy and stated failure behaviour; build one in Polars and compare code, time, memory.
- **Prove:** Argue ETL vs ELT aloud for two minutes with a cost number attached.

### Week 14 — Why is this slow
- **Python:** cProfile, timeit; memory measurement; finding the accidental O(n²); generators as a memory fix; honest benchmarking.
- **SQL:** parser/planner/executor and statistics; EXPLAIN (ANALYZE, BUFFERS) read inside out; scan types and when a seq scan is correct; join algorithms — nested loop, hash, merge.
- **Idea:** Week 3 returns. The nested loop he timed is a plan node with a name; the dict is a hash-join node.
- **Build:** Create a genuinely slow query (join on unindexed text across 5M rows), fix it three ways. Plans before/after for five queries into PERFORMANCE.md. Profile the loader, fix the hot spot.
- **Prove:** Unseen slow query and plan — name the problem and fix it in under 20 min.

### Week 15 — Read less
- **Python:** partitioned Parquet writes; predicate pushdown; column projection; chunked writers; why columnar compresses.
- **SQL:** B-tree, composite and column order, partial, covering, unique indexes; when an index hurts; VACUUM/ANALYZE; range partitioning and pruning; isolation levels, locks, deadlock; JSONB and GIN.
- **Idea:** Every performance technique is a way of reading less. Index, partition, columnar file, pruned directory — four mechanisms, one goal.
- **Build:** Index strategy with before/after plans and write cost. Partition the attempts fact by month, demonstrate pruning. Partition the Parquet to match, show the same pruning at file level.
- **Prove:** Show pruning in a plan and in a Parquet read; explain they're the same mechanism.

### Week 16 — P3 complete, CV, bridge to scale
- **Build:** P3 complete, tagged, recorded. Loader with COPY, parameterised, batched, suite green. Mart rebuilds from Parquet in one command. CV and LinkedIn rewritten; 90-second pitch; five STAR stories.
- **GATE 2** — see `gates.md`. → Junior applications open Week 17.

---

## Stage 3 — The same thing, distributed (Weeks 17–24)

Project P2: five years of collections history, 60M attempts. Every Spark topic is introduced
against the SQL equivalent he already owns. SQL track continues at hard difficulty.

- **W17** Why Spark exists · driver/executors/partitions · lazy evaluation, DAG, jobs/stages/tasks · Spark UI · distributed systems (scaling, sharding, replication, locality, fault tolerance, CAP). *Idea: a Spark partition and a Postgres partition are the same word at different scales; what's new is that moving data costs more than reading it.* Build: the synthetic history generator.
- **W18** StructType schemas · select/filter/withColumn/cast/when/nulls · UDF serialisation cost · Spark SQL, temp views, catalog, dialect differences. *Idea: write every transformation twice and `.explain()` both — same plan.* Build: the cleansing layer.
- **W19** Join types incl. anti/semi · sort-merge vs broadcast · shuffle · wide vs narrow · skew · dedupe with row_number. *Idea: broadcast join is the Week 3 dict, shipped to every executor.* Build: the four-way join, skew created and fixed.
- **W20** groupBy/agg · approx distinct · pivots · windows at scale. *Idea: a Postgres window sorts in memory; a Spark window shuffles first.* Build: ageing buckets, vintage recovery curves, retry effectiveness — reconciled against P3.
- **W21** Partitioning on write · pruning · repartition vs coalesce · caching cost · AQE · small files · reading `.explain()`. *Idea: no indexes on a lake; layout is the only pruning you get.*
- **W22** Cluster sizing as cost · memory and shuffle config · diagnosing from the UI. Build: P2 complete, PERFORMANCE.md, tagged.
- **W23** Testing Spark code · data tests (schema, null, unique, accepted values, referential, volume, freshness) · the DE test pyramid · block vs quarantine · data contracts. *Idea: Week 7 scaled — the rule now has four possible homes.*
- **W24** Interview sprint. **GATE 3**.

---

## Stage 4 — Platform and governance (Weeks 25–34)

Project P4: the collections lakehouse. Azure and Databricks learned together, not in sequence.

- **W25** Subscriptions, RGs, tagging, Cost Management, budgets · ADLS Gen2, hierarchical namespace, ACLs · object storage vs filesystem · tiers, retention, egress · Databricks workspace, notebooks vs jobs, compute types, SQL warehouses. *Idea: storage and compute are billed separately and fail separately.*
- **W26** Entra ID, RBAC, scope inheritance · managed identity vs service principal · Key Vault · encryption · PII, GDPR erasure, audit · Unity Catalog namespace, grants, lineage, row filters, column masks. *Idea: two permission systems stacked; a gap between them is a breach.*
- **W27** Delta transaction log · ACID on object storage · time travel · MERGE · OPTIMIZE, Z-order, liquid clustering, VACUUM · schema evolution and compatibility · CDC vs snapshots · warehouse/lake/lakehouse. *Idea: MERGE is Week 5's ON CONFLICT over a lake; Z-order is Week 15's composite-index column order without an index.*
- **W28** ADF — linked services, copy activity, control flow, triggers, IR, CI/CD · Auto Loader — schema evolution, checkpoints, rescued data · Lakeflow Connect · trigger modes · late-arriving data. *Idea: a checkpoint is a watermark is a file offset is a Kafka offset.*
- **W29** Medallion · declarative pipelines · expectations (warn/drop/fail) · streaming tables vs materialised views · SCD2 in production. *Idea: expectations are constraints that don't stop the whole load; SCD2 is Week 9's latest-per-key with history kept.*
- **W30** Jobs and tasks, dependencies, retries, backfills · Azure Monitor, Log Analytics, KQL, alerts · SLIs/SLOs · freshness monitoring · runbooks. *Idea: the job succeeded and the data is six hours stale.*
- **W31** Compute vs storage · serverless vs provisioned · autoscaling and sizing · job frequency · caching · tiers and lifecycle · egress. *Idea: Week 15's "read less" is a billing strategy.* Build: halve the platform cost, measured.
- **W32** Terraform state, providers, modules, plan/apply/destroy · OIDC from Actions · Asset Bundles · environment promotion. *Idea: the test isn't whether it deploys but whether he can destroy it without fear.*
- **W33** CI for data — lint, unit, deploy bundle to test, run against fixtures, promote on tag · Fabric orientation. Build: P4 complete, tagged. Fundamentals badge.
- **W34** Interview sprint. **GATE 4**. → Mid-level applications open Week 35.

---

## Stage 5 — Real-time (Weeks 35–42)

Project P5: real-time commerce platform, retail domain.

- **W35** Brokers, topics, partitions, replication, ISR · producers and acks · keys and ordering · retention and compaction · the log as a data structure · event time vs processing time.
- **W36** Consumer groups, offsets, rebalancing · idempotent producer, transactions · schema registry, Avro/Protobuf, compatibility · Kafka Connect and Debezium · Event Hubs, throughput units, capture.
- **W37** Structured Streaming — micro-batch, triggers, readStream/writeStream, output modes, checkpoints, backpressure · exactly-once to Delta. *Idea: a stream is a batch job that never ends and remembers where it stopped.*
- **W38** Event time vs processing time · watermarks and allowed lateness · windowing (tumbling, sliding, session) · state stores · streaming joins · replay. *Idea: in batch "all the data" is a fact; in streaming it's a decision you make with a watermark.*
- **W39** Streaming failure modes · fault injection · RTO · circuit breakers, poison messages, DLQ · observability for streams · DR. Build: chaos report and harness.
- **W40** Cost of streaming at scale · batch vs micro-batch vs stream per table · latency as something you buy. Build: cost model for three latency targets.
- **W41** Publish the ARMS-derived article (~1,500 words). P5 complete.
- **W42** Interview sprint. **GATE 5**.

---

## Stage 6 — Data for AI (Weeks 43–48)

Project P6: matter and document intelligence, legal domain.

- **W43** Point-in-time correctness and leakage · feature tables · train/serve skew · MLflow · the as-of join. *Idea: SCD2 from W29 makes point-in-time joins possible; leakage is the same bug as a fan-out.*
- **W44** Document ingestion, cleaning, chunking strategies, metadata, PII redaction · building the evaluation set first. *Idea: a chunk is a grain decision.*
- **W45** Embeddings · vector stores and index types · latency vs recall · freshness SLAs · pgvector vs Vector Search vs AI Search. *Idea: a vector index is a B-tree conversation with different maths — build cost, read gain, staleness.*
- **W46** LLM as a pipeline step · structured extraction · rate limits, retries, cost budgets · confidentiality walls · AI governance in Unity Catalog. *Idea: an API with a bad SLA and a per-token bill; failure is silent and plausible, so evaluation replaces assertion.*
- **W47** Retrieval pipelines · evaluation harnesses · serving under access control · FastAPI. P6 complete.
- **W48** Interview sprint. **GATE 6**.

---

## Stage 7 — Week 49 onward

Weekly: one recorded design, five applications, hard drills, one STAR refreshed.
Monthly: one write-up published, one cost review.
Q1: Databricks DE Professional; one merged open-source PR.
Q2: P7 capstone (P4+P5+P6 under one set of SLOs with an on-call runbook); mentor one learner.
Ongoing: DP-700 only for Microsoft shops. Research proposal for the 2027 intake.
