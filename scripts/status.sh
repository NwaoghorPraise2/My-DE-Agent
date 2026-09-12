#!/usr/bin/env bash
# Quick look at where you are.  Usage: scripts/status.sh
set -uo pipefail

echo "=== progress ==="
grep -E '^\*\*(Current week|Stage)' state/progress.md || true

echo
echo "=== open weaknesses ==="
sed -n '/^## Open/,/^## Watch/p' state/weaknesses.md | grep '^-' || echo "  none"

echo
echo "=== last 5 scores ==="
tail -n 5 state/scores.csv

echo
echo "=== problems saved ==="
total=$(find solutions \( -name '*.py' -o -name '*.sql' \) 2>/dev/null | wc -l | tr -d ' ')
unsolved=$(grep -rl 'VERDICT: unsolved' --include='*.py' --include='*.sql' solutions 2>/dev/null | wc -l | tr -d ' ')
echo "  total:    ${total:-0}"
echo "  unsolved: ${unsolved:-0}   <- weakness mode reads these first"

echo
echo "=== problems asked ==="
n=$(grep -c '^| w' state/asked.md 2>/dev/null | tr -d ' ')
echo "  total: ${n:-0}"
