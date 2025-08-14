# Contributing Guidelines

Thanks for your interest in improving this project. These guidelines cover workflow, quality, security, and the responsible use of AI coding assistants (e.g. GitHub Copilot).

## 1. Quick Start Workflow
1. Fork the repository (or create a feature branch if you have push access).
2. Create a branch: `git checkout -b feat/concise-topic` (prefer [conventional commit](https://www.conventionalcommits.org/) style prefixes: feat, fix, docs, chore, refactor, test, perf, build, ci, security).
3. Make focused changes (small, reviewable increments preferred).
4. Run local checks (lint, tests, security scans if applicable).
5. Commit using conventional messages (see below).
6. Push: `git push origin feat/concise-topic`.
7. Open a Pull Request (PR) and complete the PR checklist.

## 2. Use of AI Coding Assistants
AI tools can accelerate development, but YOU remain accountable for every line merged.

Mandatory steps when using AI-generated code:
- Verification: Execute / compile / lint the suggestion. Remove unused fragments.
- Licensing: Do not paste large verbatim outputs from proprietary or unknown-licensed sources. If unsure, rewrite.
- Attribution: If a non-trivial block (> ~15 lines) is AI-generated, add a concise comment: `// Generated with AI assistant; manually reviewed` (or language equivalent) and refine as needed.
- Security Review: Inspect for injections, unsafe eval, deserialization, command execution, hard‑coded secrets, ambiguous license headers.
- Privacy: Never include secrets, personal data, internal URLs, tokens, or access keys in prompts.
- Prompt Hygiene: Prefer minimal, abstract descriptions of proprietary logic—avoid copying sensitive code into prompts.

See `AI_CODING_GUIDELINES.md` for detailed policy.

## 3. Commit Message Format (Conventional Commits)
Format: `<type>(optional scope): <short summary>`

Examples:
- `feat(auth): add OAuth2 PKCE flow`
- `fix(ci): correct codeql workflow syntax`
- `security(deps): patch vulnerable library`

Body (optional) should explain rationale, tradeoffs, and security considerations if relevant. Reference issues: `Closes #123`.

## 4. Pull Requests
Each PR should:
- Stay focused (avoid mixing unrelated changes).
- Include updated docs/tests where behavior or public surface changes.
- Pass CI (lint/tests/security scans).
- Contain a completed PR checklist (auto-inserted from template).
- Disclose substantial AI assistance in the PR description (checkbox in template).

Review Expectations:
- At least one maintainer review required (two for security-sensitive code: auth, crypto, secrets handling).
- Security-critical PRs must include a brief threat assessment (attack surface, validation, error handling, logging).

## 5. Coding & Style Standards
- Follow `STYLEGUIDE.md`.
- Keep functions small, explicit inputs/outputs. Prefer pure functions for business logic.
- Add doc comments for public APIs.
- Avoid premature optimization; document performance-critical assumptions.
- Defensive programming: validate inputs at boundaries.

## 6. Testing
- Add/expand tests for new behavior; include at least one edge case.
- For bug fixes: add a regression test failing before the fix.
- Prefer fast, deterministic tests. Skip external network calls unless mocked.

## 7. Security Practices
- Never commit secrets (use environment variables / secret stores). If leaked, rotate immediately and open a security issue (see `SECURITY.md`).
- Validate and sanitize any data that could originate from outside trust boundary.
- Handle errors without leaking sensitive internal details.
- Avoid introducing new dependencies unless justified; review their license and maintenance status.

## 8. Documentation
- Update `README.md` / relevant guides when adding or changing features.
- Changelog: Add an entry under `[Unreleased]` in `CHANGELOG.md` (use Keep a Changelog style).

## 9. Issue Reporting & Discussion
- Use issues for bugs/enhancements. Provide reproduction steps, expected vs actual, environment.
- Tag issues appropriately (e.g., `security`, `good first issue`, `help wanted`).

## 10. Code of Conduct
By participating you agree to the `CODE_OF_CONDUCT.md`.

## 11. License Acceptance
All contributions are made under the project license (see `LICENSE.md`).

## 12. Questions
Open a discussion or issue if anything is unclear.

Thank you for contributing responsibly.
