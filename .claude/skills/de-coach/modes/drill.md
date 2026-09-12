# Drill mode

Rapid, timed, one at a time. 30-45 minutes total. No teaching unless he fails.

## Shape

1. **Recall (3 questions).** From previous weeks, not this one. Pull from `state/asked.md`
   topics that are 2-6 weeks old. Short answers, 60 seconds each.
2. **Concept check (2).** This week's topic. Not definitions - consequences.
   Not "what is a LEFT JOIN" but "here's a LEFT JOIN with a WHERE on the right table.
   How many rows come back and why?"
3. **Implementation (3-5).** Timed, escalating. Python and SQL alternating.
4. **One production scenario.** Ends the session.

## Rules

- One question, wait for the answer, respond, next. Never a numbered list.
- State the time limit before each timed item.
- Wrong answer -> do not correct immediately. Ask one question that makes him find it.
- Right answer -> ask one follow-up that tests whether he knows *why*.
- Save every implementation solution to `solutions/week-NN/`.

## Weakness variant

When he says `weakness`, build the entire drill from `state/weaknesses.md`. Take the top
three open entries and construct new problems testing the same underlying skill in a
different context. Never reuse the problem that exposed the weakness.

At the end, state plainly whether each weakness looks resolved, improved, or unchanged, and
update `state/weaknesses.md` accordingly.
