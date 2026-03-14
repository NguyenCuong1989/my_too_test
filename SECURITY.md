# Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security issues seriously. If you discover a vulnerability in this project,
please **do not** open a public GitHub Issue. Instead, follow the responsible disclosure
process described below.

### How to Report

1. **Email**: Send a description of the vulnerability to the repository owner via
   GitHub's [private security advisory](https://github.com/NguyenCuong1989/my_too_test/security/advisories/new).
2. **Include the following information**:
   - Type of vulnerability (e.g., RCE, SQL injection, XSS, credential exposure)
   - File(s) or component(s) affected
   - Steps to reproduce
   - Potential impact
   - (Optional) Suggested fix or patch

### Response Timeline

| Stage                        | Target Time   |
| ---------------------------- | ------------- |
| Acknowledgement of report    | Within 48 h   |
| Initial assessment           | Within 5 days |
| Fix or mitigation released   | Within 30 days (critical), 90 days (others) |
| Public disclosure (CVE etc.) | Coordinated with reporter |

### Scope

The following are **in scope** for vulnerability reports:

- Python source code (`autonomous_operator/`, `axcontrol/`, `src/`, `factory/`)
- Docker images and compose configuration
- GitHub Actions workflows
- Dependency vulnerabilities with a direct impact on this project

The following are **out of scope**:

- Third-party services or APIs that this project integrates with
- Issues already publicly known or patched upstream

## Security Tooling

This repository uses the following automated security checks:

| Tool        | Purpose                           | Trigger              |
| ----------- | --------------------------------- | -------------------- |
| **Bandit**  | Python static code analysis       | Every push / PR / weekly |
| **pip-audit** | Python dependency CVE scanning  | Every push / PR / weekly |
| **Trivy**   | Docker image vulnerability scan   | Every push / PR      |

Reports are uploaded as GitHub Actions artifacts and, where applicable, to the
GitHub Security tab via SARIF.

## Safe Harbor

We consider responsible security research and disclosure to be consistent with
this project's development goals. We will not take legal action against
researchers who:

- Make a good-faith effort to avoid privacy violations, destruction of data, and
  interruption or degradation of services.
- Report the vulnerability before public disclosure.
- Do not exploit the vulnerability beyond the minimum necessary to confirm its
  existence.
