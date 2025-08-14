# AI Coding Guidelines

Purpose: Provide standards for responsible and secure use of AI coding assistants ("AI Assistants") when contributing to this project.

## Scope
These rules apply to all code, documentation, configuration, tests, infrastructure-as-code, and automation contributed with any AI assistance.

## Principles
1. Accountability: Human contributors are fully responsible for final outputs.
2. Transparency: Material AI assistance is disclosed in commits / PRs where meaningful (see below).
3. Security & Privacy: Prompts and outputs must not expose sensitive information.
4. Compliance: Honor project license, third-party licenses, and company/legal policies.
5. Minimalism: Only generate what you understand and can maintain.

## Allowed Use Cases
- Boilerplate scaffolding (tests, simple CRUD handlers, configuration skeletons)
- Repetitive refactors (renaming, extraction)
- Documentation draft generation (must be reviewed and corrected)
- Unit test suggestions (after human validation of relevance)

## Disallowed / Restricted Use
| Category | Policy |
|----------|--------|
| Secrets / Credentials | NEVER include secrets in prompts or commit outputs containing secrets. |
| Proprietary Algorithms | Summarize intent; do not paste source verbatim into prompts without authorization. |
| Copied Large Blocks | Avoid > ~100 contiguous lines AI-generated w/o deep review & justification. |
| License Ambiguity | Reject outputs that appear copied from unknown licensed sources. |
| Security-Sensitive Code | Require heightened manual review (see Review Intensification). |

## Prompt Hygiene
- Keep prompts concise; describe behavior over pasting large code.
- Redact identifiers that may reveal internal architecture (unless public already).
- Avoid personal or user data.

## Output Validation Checklist
Before committing AI-generated code:
- Compiles / lints cleanly.
- Tests added/updated as needed.
- No unused variables, dead blocks, TODO placeholders left unaddressed.
- No obvious security flaws (injection, unsafe eval, path traversal, race conditions, deserialization risks, timing attacks).
- Error handling is consistent with project patterns.
- Logging excludes secrets and PII.
- Dependencies introduced are necessary, reputable, and license-compatible.

## Security Review Intensification
Trigger extra review (second maintainer + threat sketch) for AI-assisted changes affecting:
- Authentication / Authorization
- Cryptography / key management
- Input parsing / deserialization
- External command execution
- File system, network, or process boundaries
- Dependency upgrade introducing native bindings or privileged ops

Threat Sketch Template (include in PR if applicable):
```
Surface: (entry points changed)
Trust Boundary Changes: (describe)
Primary Risks: (e.g., injection, leakage, DoS)
Mitigations Implemented: (validation, limiting, monitoring)
Residual Risks & Follow-ups: (list)
```

## Transparency & Attribution
- If more than ~15 lines in a function were AI-generated, add a brief inline comment: `// AI-assisted: human-reviewed` (language-appropriate syntax).
- In PR description, check the "AI assistance used" box and optionally summarize scope: "Generated initial test scaffolding; logic hand-written.".
- Do NOT attribute to specific proprietary model unless required.

## Commit & PR Conventions
- Conventional commits required (see CONTRIBUTING.md).
- For large refactors initiated via AI tooling, commit message body should include reasoning and validation approach.

## Handling Uncertain Licensing
If the output resembles well-known project code or includes license headers from unknown sources:
1. Discard it.
2. Regenerate with a prompt asking for an original implementation.
3. If still similar, implement manually.

## Tool Configuration Suggestions
(Implement as the codebase grows.)
- Add CI job: dependency vulnerability scan (e.g., `npm audit`, `pip-audit`, `safety`, `cargo audit`).
- Add SAST (CodeQL, Semgrep) for supported languages.
- Secret scanning (GitHub Advanced Security or trufflehog) on pushes & PRs.

## Metrics (Optional)
Track (no PII):
- % PRs with AI assistance
- Review turnaround for AI vs non-AI PRs
- Post-merge defect density differences

## Education
Encourage contributors to read official secure coding standards (OWASP Top Ten / ASVS) & style guide.

## Violations
Maintainers may request rework or rejection if guidelines are not followed. Repeated violations may lead to restricted contribution rights.

---
Last updated: 2025-08-14
