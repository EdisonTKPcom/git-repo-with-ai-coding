# Copilot Mirror

This directory is a minimal mirror for tools expecting `.copilot/`.
Authoritative configuration lives under `.github/copilot/`.

Key locations:
- `.github/copilot/instructions.md` – house rules
- `.github/copilot/prompt-files/` – JSON prompt definitions
- `.github/copilot/runtime/` – generated instruction bundles (CI artifact)

Update process:
1. Edit source files under `.github/copilot/`.
2. CI (ai-standards-validate) validates & (re)generates runtime files.
3. Consumers can fetch the `ai-runtime-instructions` artifact.
