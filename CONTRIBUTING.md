# Contributing Guide

Thank you for taking the time to contribute to this project! This document explains everything you need to know to get started, write tests, follow the code style, submit pull requests, and format your commits.

---

## Table of Contents

1. [Development Setup](#development-setup)
2. [Testing Guidelines](#testing-guidelines)
3. [Code Style Requirements](#code-style-requirements)
4. [Pull Request Process](#pull-request-process)
5. [Commit Conventions](#commit-conventions)

---

## Development Setup

### Prerequisites

- Python **3.11+**
- `git`
- (Optional) Docker & Docker Compose for running the full stack locally

### 1. Clone the repository

```bash
git clone https://github.com/NguyenCuong1989/my_too_test.git
cd my_too_test
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install runtime dependencies

```bash
pip install -r requirements.txt          # if it exists
```

### 4. Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### 5. Configure environment variables

Copy the example environment file and fill in your credentials:

```bash
cp .env.gemini .env
# Edit .env with your GEMINI_API_KEY, NOTION_TOKEN, etc.
```

Key variables:

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Google Gemini AI API key |
| `NOTION_TOKEN` | Notion integration token |
| `NOTION_DB_ID` | Target Notion database ID |
| `GOOGLE_TOKEN_PATH` | Path to `token.json` (default: `token.json`) |
| `GOOGLE_CREDENTIALS_PATH` | Path to `credentials.json` (default: `credentials.json`) |
| `LOG_LEVEL` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |

---

## Testing Guidelines

### Running the test suite

```bash
# Run all tests with coverage report
pytest

# Run a specific test file
pytest tests/test_utils/test_helpers.py

# Run tests matching a keyword
pytest -k "test_coordinator"

# Skip slow or integration tests
pytest -m "not slow and not integration"
```

### Coverage target

The project targets **≥ 70% code coverage**. `pytest.ini` is configured to enforce this automatically with `--cov-fail-under=70`. A detailed HTML report is generated in `htmlcov/` after each run.

### Writing new tests

- Place unit tests in `tests/test_core/`, `tests/test_utils/`, etc., mirroring the `src/` layout.
- Use integration tests in `tests/test_integration.py` when multiple modules interact.
- Prefer `unittest.mock.MagicMock` / `pytest-mock` over real external service calls.
- Share common fixtures in `tests/conftest.py`.
- Aim for one `assert` per logical concept to keep failures informative.

### Test file naming

| Test type | Location | Naming |
|---|---|---|
| Unit | `tests/test_<module>/` | `test_<source_file>.py` |
| Integration | `tests/` | `test_integration.py` |
| Smoke | `tests/` | `test_smoke.py` |

---

## Code Style Requirements

This project uses **Black** for formatting and **Flake8** for linting.

### Format code

```bash
black src/ tests/
```

### Lint code

```bash
flake8 src/ tests/
```

### Configuration

- `black` is configured with its defaults (line length 88).
- `flake8` should respect the project's `.flake8` or `setup.cfg` if present; otherwise the default settings apply (max line length 88 to match Black).

### Type checking (optional but encouraged)

```bash
pyright src/   # or: pyre check
```

A `pyrightconfig.json` is already present in the repository root.

### General guidelines

- Use **type hints** on all public function signatures.
- Write **docstrings** for public modules, classes, and functions (Google style).
- Avoid bare `except:`; always catch specific exception types or use `except Exception`.
- Do not commit secrets or credentials to the repository.

---

## Pull Request Process

1. **Fork** the repository and create a feature branch from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
2. Make your changes following the [Code Style Requirements](#code-style-requirements).
3. Add or update **tests** to cover your changes. Ensure coverage stays ≥ 70 %.
4. Run the full test suite locally and confirm it passes:
   ```bash
   pytest
   ```
5. Run the linter and formatter:
   ```bash
   black src/ tests/
   flake8 src/ tests/
   ```
6. Push your branch and open a **Pull Request** against `main`.
7. Fill in the PR template (if provided) with:
   - A clear description of *what* changed and *why*.
   - Reference to any related issue (e.g., `Closes #42`).
   - Screenshots or logs for UI / behavioural changes.
8. At least one maintainer review is required before merging.
9. Squash commits on merge to keep the history clean.

---

## Commit Conventions

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

### Types

| Type | When to use |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `style` | Formatting, missing semicolons, etc. (no logic change) |
| `refactor` | Code change that is neither a fix nor a feature |
| `test` | Adding or correcting tests |
| `chore` | Build process, dependency, or tooling changes |
| `perf` | A code change that improves performance |

### Examples

```
feat(coordinator): add Notion lead logging support

fix(helpers): handle empty string in parse_json_string

docs(contributing): add commit convention section

test(diagnostic): cover framework load failure path

refactor(synergy): extract SynergyOperator into dedicated class
```

### Rules

- Use the **imperative mood** in the summary line ("add", not "added" or "adds").
- Keep the summary line under **72 characters**.
- Reference issues and PRs in the footer:
  ```
  Closes #12
  See-also: #8
  ```
- Do **not** include secrets, passwords, or API keys in any commit message or file.
