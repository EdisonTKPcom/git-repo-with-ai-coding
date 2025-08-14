# Changelog

All notable changes to this project will be documented here.

## [Unreleased]
### Added
- AI coding guidelines (`AI_CODING_GUIDELINES.md`)
- Code review guidelines (`CODE_REVIEW.md`)
- PR template enforcing AI & security disclosures
- CI workflow with lint/test skeleton, secret scan, dependency audit, CodeQL
- Enhanced security policy & contributing guidelines
- CODEOWNERS for enforced review ownership
- Dependabot configuration for dependencies & GitHub Actions
- EditorConfig for consistent formatting
- Commitlint + Husky + pre-commit hooks (lint, basic secret scan)
- Semgrep SAST rules baseline
- OSS Review Toolkit config stub
- Sample source (`src/index.js`) and tests (`test/greet.test.js`) to exercise CI
 - ESLint configuration (.eslintrc.cjs)
 - Added Semgrep & ORT jobs to CI
 - Security issue template
 - README badges and security/tooling sections
 - SPDX license header enforcement script & CI check
 - ORT result artifact upload & SPDX in CI
 - Semgrep badge placeholder
 - Bug & Feature issue templates
 - License/semgrep npm scripts

## [1.0.0] - 2025-08-14
- Initial release
