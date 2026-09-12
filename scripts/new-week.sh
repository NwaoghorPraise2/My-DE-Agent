#!/usr/bin/env bash
# Scaffold a week's solution folder.  Usage: scripts/new-week.sh 03
set -euo pipefail

[ $# -eq 1 ] || { echo "usage: $0 <week number, zero padded e.g. 03>"; exit 1; }
W="$1"
DIR="solutions/week-${W}"

mkdir -p "${DIR}/python" "${DIR}/sql"

[ -f "${DIR}/INDEX.md" ] || cat > "${DIR}/INDEX.md" <<INDEX
# Week ${W} — solutions

| id | problem | lang | limit / taken | verdict | key idea |
|---|---|---|---|---|---|
INDEX

[ -f "${DIR}/NOTES.md" ] || cat > "${DIR}/NOTES.md" <<NOTES
# Week ${W} — notes

## The one idea this week

## What I got wrong

## What I'd do differently

## Still unclear
NOTES

echo "scaffolded ${DIR}"
