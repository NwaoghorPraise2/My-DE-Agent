# DE Training

A training repo that doubles as a coach. Claude Code reads the curriculum, tests you,
and writes what happened back to disk so the next session knows where you are.

## First time

```bash
git clone git@github.com:<you>/de-training.git
cd de-training
claude
```

Then say: **`start week 1`**

## Every session after that

```bash
cd de-training
claude
```

Say one of: `drill` · `build` · `debug` · `design` · `interview` · `gate` · `weakness` · `review`

The coach reads `state/` first, so it always knows your week, your open gaps and
every problem you have already been given.

## What lives where

| Path | What it is |
|---|---|
| `.claude/skills/de-coach/` | The coach itself. Edit `SKILL.md` to change how it behaves. |
| `curriculum/week-by-week.md` | What you learn each week, and the pairing behind it. |
| `curriculum/gates.md` | The six progression gates. |
| `state/progress.md` | Current week, gate status, level per competency. |
| `state/weaknesses.md` | Recurring mistakes, dated. Drives what you get asked. |
| `state/scores.csv` | One row per graded assessment. |
| `state/asked.md` | Every problem already used, so nothing repeats. |
| `solutions/week-NN/` | Your accepted solutions, saved automatically. |
| `log/YYYY-MM-DD.md` | Session transcript summary. |
| `notes/` | Your concept cards. |

## Committing

The coach stages your solutions and state updates at the end of a session and tells
you the commit command. It never pushes for you.

```bash
git add -A && git commit -m "week 03: hash join katas, 7/10" && git push
```
