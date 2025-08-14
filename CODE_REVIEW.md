# Code Review Guidelines

Purpose: Ensure consistent, secure, maintainable contributions and responsible AI-assisted code integration.

## Review Objectives
1. Correctness
2. Security & privacy
3. Maintainability & readability
4. Performance (only if relevant scope)
5. Test adequacy
6. Architectural consistency

## Reviewer Checklist
- Scope: Single logical concern? If not, request split.
- Build: Does it pass lint/tests locally or in CI? (Block if red.)
- Style: Conforms to `STYLEGUIDE.md`.
- Docs: README / inline docs updated where necessary.
- Changelog: Updated under `[Unreleased]` if user-facing change.
- Tests: Cover happy path + at least one edge / error condition.
- Public APIs: Clear naming & doc comments.
- Dependencies: New dependencies justified, minimal, reputable, license-compatible.
- Logging & Errors: No sensitive info; errors actionable.
- Config / Secrets: No secrets committed.
- AI Attribution: PR checklist box ticked if AI assistance used; inline comments where substantial AI code present.

## Security-Focused Checklist
Apply always; intensify for sensitive areas (auth, crypto, validation, serialization, file/network IO):
- Input Validation: Proper sanitation & type checks.
- Output Encoding: Where applicable (templates, HTML, shell commands).
- Injection Risks: No dynamic SQL/command concat; parameterization used.
- AuthZ: Access controls enforced at entry points.
- Sensitive Data: Not logged; redaction in place.
- Error Messages: Non-revealing; no stack traces in production paths.
- Resource Use: No obvious unbounded loops, memory, or concurrency hazards.
- Race Conditions: Concurrency primitives used where needed.
- Third-Party Code: License & security posture reviewed.

## Performance Considerations
- Only request optimizations if there's evidence of impact or big-O regression.
- Add micro-benchmarks only when justified.

## AI-Assisted Code Review Extras
- Smell Detection: Over-generalized abstractions, duplicate generic comments, placeholder names.
- Verify untested auto-generated code manually.
- Ensure generated comments actually match logic.

## Review Tone & Process
- Be respectful & specific.
- Prefer guiding questions over directives when subjective.
- Provide actionable suggestions or examples.
- Approve with “nit” comments if only minor stylistic issues remain.

## Approvals
- Minimum: 1 maintainer approval.
- Security-sensitive: 2 approvals (one with security experience).

## Post-Merge Responsibilities
- Monitor CI for delayed failures (flaky tests) within 24h.
- Revert quickly if critical regression appears.

---
Last updated: 2025-08-14
