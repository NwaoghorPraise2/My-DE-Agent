# Solution file format

One file per problem. Self-contained: statement, attempt, verdict, lesson. It must be
possible to re-attempt the problem cold from this file alone, with the solution scrolled off
the screen.

## Python

```python
"""
w03-p04 · top-n-by-exposure
===============================================================================
PROBLEM
You have a list of 500,000 collection attempt dicts, each with account_id and
amount_pence. Return the 20 accounts with the highest total exposure, highest
first. Ties broken by account_id ascending.

CONSTRAINTS
- Single pass over the input where possible
- Do not sort all 500,000 accounts
- amount_pence is an int; totals must not overflow into float

EXAMPLE
in:  [{"account_id": "A1", "amount_pence": 500},
      {"account_id": "A2", "amount_pence": 300},
      {"account_id": "A1", "amount_pence": 200}]
top 1 -> [("A1", 700)]

EDGE CASES GIVEN
- empty input
- fewer than 20 distinct accounts
- an account appearing once with amount 0

-------------------------------------------------------------------------------
MODE: drill            DATE: 2026-09-24
TIME LIMIT: 15 min     TAKEN: 21 min      HINTS USED: 1 (direction)
VERDICT: correct, second attempt

FIRST ATTEMPT WENT WRONG BY
Building the totals with a list of (id, total) tuples and scanning it for each
row -> O(n²). Ran 40s on 500k. Second attempt used a defaultdict, 0.6s.

WHY THE FIX WORKS
Dict lookup is O(1) amortised; the scan was O(n). heapq.nlargest is O(n log k)
against a full sort's O(n log n) — with k=20 and n=400k that is the difference
that matters, not the aggregation.

CONNECTS TO
Week 3 hash join · Week 6 GROUP BY · Week 19 broadcast join

STILL UNSURE ABOUT
Whether nlargest's tie-breaking is stable — did not verify.
===============================================================================
"""

from collections import defaultdict
import heapq


def top_n_by_exposure(attempts, n=20):
    totals = defaultdict(int)
    for a in attempts:
        totals[a["account_id"]] += a["amount_pence"]
    return heapq.nlargest(n, totals.items(), key=lambda kv: (kv[1], kv[0]))


# --- tests ---------------------------------------------------------------
def test_empty():
    assert top_n_by_exposure([]) == []
```

## SQL

Same block, in a `/* */` comment. Add the evidence that proves it right.

```sql
/*
w03-p07 · collections-with-no-return
===============================================================================
PROBLEM
<verbatim>

CONSTRAINTS
<verbatim>

-------------------------------------------------------------------------------
MODE: drill            DATE: 2026-09-24
TIME LIMIT: 10 min     TAKEN: 8 min       HINTS USED: 0
VERDICT: correct

FIRST ATTEMPT WENT WRONG BY
Used NOT IN against a nullable column — returned zero rows silently.

EVIDENCE
input 412,338 attempts · 409,901 matched · 2,437 unmatched
plan: Hash Anti Join, 180ms (was Seq Scan + SubPlan, 14s)

CONNECTS TO
Week 3 anti join · Week 7 NULL three-valued logic · Week 14 plan reading
===============================================================================
*/

SELECT a.collection_ref, a.account_id, a.amount_pence
FROM   collection_attempt a
WHERE  NOT EXISTS (
         SELECT 1 FROM collection_return r
         WHERE  r.collection_ref = a.collection_ref
       );
```

## Unsolved problems

Save them. Set `VERDICT: unsolved` and keep the partial attempt.

```
VERDICT: unsolved — ran out of time at 15 min with the grouping done
STUCK AT
Could not see how to get top-N without sorting everything. Knew heapq existed,
could not connect it to the problem.
WHAT WOULD HAVE UNBLOCKED ME
Naming the complexity target out loud: "O(n log k), not O(n log n)".
RETEST: week 6, different context (top products by revenue)
```

These are the most useful files in the repo. `weakness` mode reads them first.

## Bridge challenges

One file per language, same id, cross-referenced, plus a `RECONCILIATION` block in both:

```
RECONCILIATION
Python: 2,437 rows   SQL: 2,441 rows   -> DISAGREED
Cause: Python compared refs case-sensitively; the source pads with trailing
spaces on re-presentations. SQL's = ignores nothing, so the bug was mine in
Python. Fixed by stripping on parse, not on compare.
```

Never resolve a disagreement for him. Make him find it, then record what he found.
