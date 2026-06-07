# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`immune-cli` is a Python command-line tool. This repository is in early initialization — update this file as the project structure takes shape.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Common Commands

Update these once the project structure is defined:

| Task | Command |
|------|---------|
| Run CLI | `immune <subcommand>` |
| Run tests | `pytest` |
| Run single test | `pytest tests/path/to/test.py::test_name -v` |
| Lint | `ruff check .` |
| Format | `ruff format .` |
| Type check | `mypy .` |
