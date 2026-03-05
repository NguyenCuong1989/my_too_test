# my_too_test

Skeleton generated via Mobile-First Tool-Orchestrated Build Method.

[![Security Scanning](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/security.yml/badge.svg)](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/security.yml)
[![Code Coverage](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/coverage.yml/badge.svg)](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/NguyenCuong1989/my_too_test/branch/main/graph/badge.svg)](https://codecov.io/gh/NguyenCuong1989/my_too_test)
[![No-Drift Gate](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/no-drift-gate.yml/badge.svg)](https://github.com/NguyenCuong1989/my_too_test/actions/workflows/no-drift-gate.yml)

## Run

```bash
python3 src/main.py
```

## Docker

Production deployment uses a single consolidated compose file with environment profiles.

```bash
# Production
docker compose -f docker-compose.prod.yml --profile production up -d

# Debug
docker compose -f docker-compose.prod.yml --profile debug up

# Development (includes firebase emulator)
docker compose -f docker-compose.prod.yml --profile development up -d
```

### Environment variables

Copy `.env.gemini` as a starting point and set the required secrets:

| Variable              | Required | Description                    |
| --------------------- | -------- | ------------------------------ |
| `JWT_SECRET`          | ✅        | JWT signing secret             |
| `GOOGLE_CLOUD_PROJECT`| optional | GCP project ID                 |
| `NODE_ENV`            | optional | `production` / `development`   |

## Dependencies

| File                      | Purpose                              |
| ------------------------- | ------------------------------------ |
| `requirements.txt`        | Main runtime dependencies            |
| `requirements-dev.txt`    | Development tools (linting, docs)    |
| `requirements-test.txt`   | Testing & coverage tools             |
| `requirements-docker.txt` | Container-specific extras            |

```bash
# Install for development
pip install -r requirements-dev.txt

# Install for testing
pip install -r requirements-test.txt
```

## Testing & Coverage

```bash
# Run all tests with coverage report (≥70% required)
pytest

# Run only axcontrol no-drift invariants
AXCONTROL_SIM=1 python3 -m unittest axcontrol/tests/test_bridge_no_drift -v
```

## Security

Security scanning runs automatically on every push/PR and weekly:

- **Bandit** – Python static code analysis (`bandit.yaml`)
- **pip-audit** – Dependency CVE scanning (`.safety-config.json`)
- **Trivy** – Docker image vulnerability scanning

See [SECURITY.md](SECURITY.md) for the vulnerability disclosure policy.
