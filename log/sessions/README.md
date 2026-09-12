# Session transcripts

One file per session: `YYYY-MM-DD-HHMM-weekNN.md`.

Written turn by turn, **live, during the session** — never batched to the end. If a session
gets interrupted (crash, closed terminal, connection drop), everything up to the last
completed turn is already on disk, and `state/session-current.md` points at this file with
`Status: in-progress`, so the next session resumes from exactly where it stopped instead of
losing the thread.

## Format

```
# Session — 2026-09-12 17:40 — Week 1

Status: in-progress
Mode: default

---

## Turn 1
**Q:** <verbatim question posed>

**Praise:** <verbatim answer, or the code/SQL he submitted>

**Feedback:** <the coach's response — correct or not, why, hints given, what's still missing>

**Verdict:** correct | partial | incorrect | unsolved

---

## Turn 2
...
```

`Status` flips to `completed` once the session's end-of-session writes
(`state/asked.md`, `state/weaknesses.md`, `state/progress.md`, `log/YYYY-MM-DD.md`) are done.
The daily `log/YYYY-MM-DD.md` summary is a roll-up of this file's turns, not a
from-memory reconstruction — write the transcript first, summarize from it second.
