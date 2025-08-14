# Security Context (#security)

Security posture & required considerations.

Controls:
- CI: CodeQL, Semgrep, secret scan, SPDX/license check, dependency audit.
- Policy: SECURITY.md defines disclosure, severity SLAs.
- Pre-commit: secret heuristic + lint.

Checklist Highlights:
- Input validation at boundaries.
- No secrets / credentials in code or logs.
- Avoid `eval`, unsanitized shell, path traversal.
- Review dependency licenses & vulnerability status.

Threat Sketch Template:
Surface | Trust Boundary Changes | Risks | Mitigations | Residual Risk
