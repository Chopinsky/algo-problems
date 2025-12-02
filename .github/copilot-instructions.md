# Copilot Instructions for `algo-problems`

This guide helps AI coding agents work productively in the `algo-problems` codebase. It summarizes architecture, workflows, and conventions unique to this repository.

## Project Overview
- Multi-language solutions for algorithmic problems (LeetCode, HackerRank, Meta, etc.)
- Main languages: Go (`main.go`, `go/`, `go-old/`, `p0/`), Python (`main.py`, `challenges/`, `meta_puzzles/`, `misc/`), JavaScript (`js-problems/`)
- Each language has its own entry point and conventions for running solutions.

## Directory Structure
- `go/`, `go-old/`, `p0/`, `p1/`: Go solutions, organized by problem number or topic
- `js-problems/`: JavaScript solutions, each in its own folder, with a shared runner (`main.js`)
- `challenges/`, `meta_puzzles/`, `misc/`: Python scripts for specific problems or experiments
- `hacker_rank/`: Python solutions for HackerRank problems

## Running Solutions
- **Go:**
  - Run with: `go run . -n=<problem_number>` from project root
  - Problems are referenced by number (see `main.go` and `Problems/`)
- **JavaScript:**
  - Run with: `node ./js-problems/main.js <ProblemName> [--debug]`
  - Each problem is a folder in `js-problems/`, default is `FreqStack`
- **Python:**
  - No unified runner; run scripts directly (e.g., `python challenges/hanoi_tower.py`)

## Developer Workflows
- **Build:**
  - Go: Use `go-build` npm script if present, or standard Go commands
- **Test:**
  - No global test runner; tests may be embedded in problem files or subfolders
- **Debug:**
  - JS: Use `--debug` flag with runner
  - Go/Python: Add print statements or use language-specific debuggers

## Conventions & Patterns
- Solutions are grouped by problem number or topic, not by language features
- Minimal external dependencies; most code is self-contained
- Solution files often named as `<ProblemNumber>.<Description>.<ext>`
- Shared utilities may exist in `Utils/` (Go) or similar folders
- Problems may have multiple versions (see `go-old/` vs `go/`)

## Integration Points
- No major service boundaries; code is organized for individual problem solving
- No database or network integration
- External dependencies are rare; check `package.json` for JS, `go.mod` for Go

## Examples
- To run Go problem 685: `go run . -n=685`
- To run JS problem `FreqStack` in debug: `node ./js-problems/main.js FreqStack --debug`
- To run Python script: `python challenges/hanoi_tower.py`

## Key Files
- `main.go`, `main.py`, `js-problems/main.js`: Entry points for each language
- `README.md`: Basic usage and running instructions
- `Problems/`, `Utils/`, `js-problems/`: Core solution directories

---

If any conventions or workflows are unclear, please provide feedback so this guide can be improved.