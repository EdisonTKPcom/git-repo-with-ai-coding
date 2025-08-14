# Project Name

![CI](https://github.com/username/project-name/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/username/project-name/actions/workflows/ci.yml/badge.svg?label=CodeQL)
![Semgrep](https://img.shields.io/badge/semgrep-configured-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Short one-line description of your project.

## 🚀 Features
- Feature 1
- Feature 2
- Feature 3

## 📦 Installation
```bash
git clone https://github.com/username/project-name.git
cd project-name
npm install
```

## 🛠 Usage
```bash
npm start
```

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for workflow and [AI_CODING_GUIDELINES.md](AI_CODING_GUIDELINES.md) for responsible AI-assisted development standards.

## 🤖 AI Coding (Using GitHub Copilot & Other Assistants)
Responsible AI assistance speeds development while keeping you accountable for every line merged. This section is a practical quick-start; the full policy lives in `AI_CODING_GUIDELINES.md`.

### 1. Allowed & Typical Uses
- Boilerplate: config scaffolds, test skeletons, repetitive refactors.
- Draft docs / comments (must review & adapt tone/details).
- Generating alternative implementations for comparison.

### 2. Restricted / Extra Review Areas
Changes touching authentication, authorization, crypto, input parsing, file / network IO, or privilege boundaries require a second reviewer and (if non‑trivial) a brief threat sketch in the PR description.

### 3. Prompt Hygiene (DO NOT include)
- Secrets / tokens / private URLs / credentials.
- Large proprietary source blocks (describe intent instead).
- Personal or sensitive user data.

### 4. Validation Checklist BEFORE Committing AI Output
Run through quickly; reject or rewrite if any fail:
1. Lints clean: `npm run lint` (or fixed with `--fix`).
2. Tests added/updated and pass: `npm test`.
3. No obvious security smells (eval, unsanitized input, path traversal, command concat, insecure random, hard‑coded secrets).
4. Logic is understood (no “mystery” code) & simplified where possible.
5. Licenses: No copied code with ambiguous headers or incompatible license text.
6. Comments accurately describe the final implementation.

### 5. Commit & PR Disclosure
- If a substantial block (> ~15 contiguous lines or core algorithm) originated from AI, add a short inline comment: `// AI-assisted: human-reviewed`.
- In the PR template, tick the “AI assistance used” checkbox and summarize scope (e.g. “Generated initial test scaffolding; logic refactored manually”).
- Keep conventional commit types (e.g. `feat:`, `fix:`, `chore:`). A dedicated `security:` type is allowed.

### 6. Minimal Example Workflow
```bash
# 1. Generate a draft (in editor with Copilot)
# 2. Manually inspect & trim unused pieces
npm run lint
npm test
# (Optional) Run SAST locally if semgrep installed
npm run semgrep
git add <changed files>
git commit -m "feat: add greet helper (AI-assisted: test scaffold)"
git push && open PR
```

### 7. Threat Sketch (Only if Sensitive)
Include in PR for sensitive domains:
```
Surface: <entry points / files>
Trust Boundary Changes: <describe>
Primary Risks: <list>
Mitigations Implemented: <validation / limits>
Residual Risks & Follow-ups: <list>
```

### 8. Quick Security Heuristics
- All external input validated early; fail fast.
- Avoid dynamic string building for shell/SQL/paths—prefer APIs.
- No silent catch-and-ignore of errors.
- Log events, not secrets.

### 9. Common Rejections
Reject AI output that is: overly abstract for scope, duplicates existing utilities, introduces unused parameters, or adds heavy dependencies for trivial tasks.

### 10. Questions
Open a discussion or issue; tag with `ai-assist` if relevant.

> You are always the human reviewer of AI drafts—treat them as suggestions, not authority.

## 🔐 Security
Please report vulnerabilities via the security issue template or email security@example.com. See [SECURITY.md](SECURITY.md).

## 🧪 Quality & Security Tooling
- CI: Lint (ESLint v9 flat config), tests, secret scan, dependency audit, CodeQL, Semgrep, SPDX header & license scan (ORT)
- Pre-commit: lint-staged (auto-fixable lint), secret heuristic
- Dependency updates: Dependabot (npm & GitHub Actions)
- Automated license & security: ORT + CodeQL + Semgrep + npm audit (0 known vulns as of last update)

Run lint locally:
```bash
npm run lint
```

Run tests:
```bash
npm test
```

Security / SAST locally (requires semgrep installed via pip):
```bash
pip install --upgrade semgrep
npm run semgrep
```

## 📄 License
This project is licensed under the MIT License — see [LICENSE](LICENSE.md) for details.
