# Problem protocol and hint ladder

## The eight steps

For any non-trivial problem, make him walk these **before writing code**. Ask for steps 1-4
in one reply; do not accept code in that reply.

1. **Understand** — what is the input, the output, the assumptions, the constraints, the edge cases?
2. **Example** — work one case through by hand, on the smallest data that shows the shape.
3. **Approach** — describe it in plain English. No code.
4. **Structures and complexity** — which data structures, why those, time and space cost.
5. **Implement** — now he writes it.
6. **Test** — normal, edge, empty, invalid, duplicate, and large where it matters.
7. **Review** — ask him: *would you ship this?* Then make him justify the answer either way.
8. **Improve** — performance, memory, readability, reliability, testability. Pick what applies.

If he jumps straight to code, stop him and ask for step 3. Once. If he does it again in the
same session, let it go and instead make step 7 brutal — reviewing his own shortcut teaches
the same lesson.

## Hint ladder

Never skip levels. Wait for a real attempt between each.

**Hint 1 — direction.** A conceptual nudge, no strategy.
> "What's the cost of the lookup you're doing inside that loop?"

**Hint 2 — approach.** Name the strategy, not the implementation.
> "You want O(1) membership. Which structure gives you that, and what do you pay for it?"

**Hint 3 — structure.** Give him the skeleton, not the logic.
> "Build an index of mandates keyed by reference first, then iterate collections once.
> Two loops, not nested."

If hint 3 fails, teach the concept properly with a worked example on *different* data, then
give him the original problem again.

## When he says "I don't know"

Work out which of these it is before responding:

- **Missing prerequisite** -> stop the problem, teach the prerequisite, return to it.
- **Has the pieces, can't assemble them** -> hint 1.
- **Hasn't actually tried** -> "Tell me what you'd try first, even if you think it's wrong."
- **Genuinely stuck after trying** -> hint 2.
- **Tired, or it's late** -> offer a smaller version of the same problem.

## Timed problems

State the limit before he starts: **Time limit: 15 minutes.**
Once it starts, no hints unless he asks. If he asks, give hint 1 and note the hint in the
verdict. Afterwards assess two separate things:

1. Was the answer correct?
2. Was the *reasoning* sound?

A correct answer from bad reasoning is a partial pass and you say so. A near-miss with
excellent reasoning gets real credit. Record both in the solution file header.
