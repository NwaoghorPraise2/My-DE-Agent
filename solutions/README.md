# Solutions

One folder per week, one file per problem. The coach writes these during the session.

```
week-03/
  INDEX.md                         one line per problem
  python/04-top-n-by-exposure.py
  sql/07-collections-with-no-return.sql
  NOTES.md                         week-level reflections
```

**Every file contains the problem, not just the answer.** The header block holds the verbatim
statement, the constraints, a worked example, the time limit and time taken, hints used, the
verdict, and what went wrong on the first attempt. You can re-attempt any problem cold from
its own file by scrolling past the header.

**Unsolved problems are saved too**, with `VERDICT: unsolved` and the point you got stuck.
Those are the ones `weakness` mode feeds on.

Format spec: `.claude/skills/de-coach/references/solution-format.md`
Scaffold a week manually: `scripts/new-week.sh 03`

## Re-attempting cold

```bash
# strip the solution, keep the problem
sed -n '/^"""/,/^"""/p' solutions/week-03/python/04-top-n-by-exposure.py
```

Or just say `redo w03-p04` and the coach will give you the problem back without the answer.
