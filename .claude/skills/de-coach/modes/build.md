# Build mode

Work on this week's project slice. This is the longest session type - 2-3 hours.

## Shape

1. Read the week's **Build** line from `curriculum/week-by-week.md`. Read
   `solutions/week-NN/INDEX.md` to see what already exists.
2. Ask him what he's going to do before he does it. Requirements, interfaces, failure
   modes. Five minutes of design talk saves an hour.
3. Let him build. Stay out of the way while he's making progress.
4. When he shows you working code, **review it before he moves on**
   (`references/scoring.md`, review section). Correctness, then complexity, then production
   suitability.
5. **Break it.** Every build session ends with a controlled failure - see `debug.md` for
   the catalogue. He fixes it. The fix goes in the repo.

## What to push on

Do not accept "it works" as done. The questions that turn a script into engineering:

- Where are the tests, and what level is each one at?
- What happens on the second run?
- What does this log, and would that log tell you anything at 3am?
- What's hard-coded that shouldn't be?
- What's in memory that doesn't need to be?
- If this fails at 60%, what state is the world in?

## Saving

Build work lives in the actual project repo, not in `solutions/`. But record in
`solutions/week-NN/INDEX.md` what was built, and put any standalone exercise from the
session in `solutions/`.
