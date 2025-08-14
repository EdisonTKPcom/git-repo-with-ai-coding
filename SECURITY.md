# Security Policy

We take security seriously and appreciate coordinated disclosure.

## Reporting a Vulnerability
Email: security@example.com (use an encrypted channel if possible). Provide:
- A clear description of the issue & potential impact
- Steps to reproduce (minimal PoC)
- Affected versions / commit hashes
- Suggested remediation if known

We will acknowledge receipt within 3 business days and aim to provide a remediation timeline after initial triage. Please do not publicly disclose before a fix is released (or 90 days, whichever sooner) unless mutually agreed.

## Scope
All code and configuration in this repository. Third-party dependencies should be reported upstream when appropriate; feel free to CC us if impactfully exploitable here.

## Non-Qualifying Issues (Examples)
- Missing security headers on non-production demo assets
- Denial-of-service requiring unrealistic resource exhaustion
- Vulnerabilities in unsupported dependencies with available patches already

## Secure Development Lifecycle (SDL)
We integrate security throughout development:
- PR Template requires security considerations section
- Mandatory input validation & error handling review
- Automated CI: secret scanning, dependency audit, static analysis (CodeQL), optional SAST tools
- AI-generated code undergoes extra scrutiny (see `AI_CODING_GUIDELINES.md`)

## Secret Handling
- No secrets committed (scans enforced in CI)
- Use environment variables / secret managers for local + deployment
- Rotate credentials immediately upon suspected leak and open a private security issue

## Dependency Management
- Prefer minimal, actively maintained dependencies
- High/Critical vulnerabilities flagged must be addressed or mitigated before release

## Responsible Use of AI Assistance
AI tools must not introduce:
- Insecure patterns (unsafe eval, injection vectors, unvalidated input)
- Copied code with unknown or incompatible licenses
See `AI_CODING_GUIDELINES.md`.

## Reporting Channels
Primary: security@example.com
Fallback: Open a GitHub security advisory draft (if repository supports it) or contact a maintainer via private channel.

## Bug Bounty
No formal bounty program currently. High-impact reports may receive public acknowledgment (opt-in).

## Timeline Targets
| Severity | Target Fix / Mitigation |
|----------|-------------------------|
| Critical | 7 days |
| High     | 14 days |
| Medium   | 30 days |
| Low      | 60 days |

## After Remediation
- Add regression tests where feasible
- Update documentation / hardening guides
- Credit reporter (if desired)

Thank you for helping keep the project secure.
