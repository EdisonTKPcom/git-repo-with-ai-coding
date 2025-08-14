# AI Assistant House Rules

Concise, enforceable rules for GitHub Copilot / agentic workflows.

## Principles
1. Human accountability: you (the developer) own all merged output.
2. Least privilege & minimalism: generate only what’s needed.
3. Security-first: no secrets, unsafe eval, or license violations.
4. Transparency: disclose meaningful AI assistance in PRs.
5. Reusability: prefer shared prompts, extensions, and commands over ad hoc long prompts.

## Mandatory Checks Before Commit
- Lint + tests green.
- No secrets / keys / tokens in diff.
- Added or updated tests for new logic or bug fixes.
- Security-sensitive areas reviewed by second maintainer.

## Prompt Hygiene
- Describe behavior & constraints; avoid pasting large proprietary code blocks.
- Redact internal identifiers unless already public.
- DO NOT include credentials, internal URLs, user data, or tokens.

## AI Attribution
- Inline comment `// AI-assisted: human-reviewed` for substantial (>15 lines or core algorithm) generated blocks.
- PR description: tick AI assistance box + brief scope summary.

## Disallowed Patterns
- Copying license-incompatible code.
- Introducing dependencies without justification (performance, security, maintenance, license).
- Cryptography / auth logic generated without manual redesign & review.

## Escalation Triggers (Require Threat Sketch)
- AuthN/AuthZ, crypto, deserialization, command/file/network boundary, privilege changes.

Include threat sketch with: Surface, Trust Boundaries, Risks, Mitigations, Residual Risk.

---
Last updated: 2025-08-14
