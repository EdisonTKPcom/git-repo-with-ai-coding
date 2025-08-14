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
