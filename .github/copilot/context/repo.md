# Repository Context (#repo)

High-level repository description for AI prompts.

- Language: Node.js (ESM)
- Tooling: ESLint v9 (flat), Semgrep, CodeQL, Husky hooks, commitlint, ORT license scanning.
- Primary sample code: `src/index.js` greeting utility.
- Tests: Node test runner in `test/`.
- Policies: See SECURITY.md, AI_CODING_GUIDELINES.md, CODE_REVIEW.md.

Key Expectations:
- Maintain minimal dependencies.
- Enforce security lint & static analysis cleanliness.
- All changes need tests when behavior changes.
