# Style Guide

Baseline conventions for this project. See also `CODE_REVIEW.md` for review criteria.

## Formatting
- Indentation: 4 spaces.
- Line length: Aim <= 100 chars (soft limit) unless readability improves otherwise.
- Trailing whitespace: Remove.

## Naming
- Variables/functions: `lowerCamelCase` (or idiomatic for language ecosystem).
- Constants: `UPPER_SNAKE_CASE`.
- Classes / Types: `PascalCase`.
- Filenames: consistent with language norms (e.g., `kebab-case` for config, `lowerCamelCase` or `snake_case` otherwise).

## Comments & Documentation
- Public APIs: Brief doc comment with purpose, parameters, return, error conditions.
- Avoid redundant comments that restate code.
- Document rationale for non-obvious decisions, performance tradeoffs, and security-sensitive logic.

## Structure & Readability
- Prefer small, cohesive functions.
- Early returns over deeply nested conditionals.
- Separate pure logic from side effects when feasible.

## Error Handling
- Fail fast on programmer errors; handle expected runtime errors gracefully.
- Provide actionable error messages without leaking sensitive data.

## Testing Conventions
- Test file naming: mirror source file naming with suffix (e.g., `*.test.*`).
- One assertion concept per test where reasonable; use descriptive test names.

## Performance Guidelines
- Measure before optimizing; include benchmark or profile link in PR if optimization-focused.

## Security Hygiene
- Sanitize/validate external input at boundaries.
- Avoid unsafe dynamic evaluation, shelling out without necessity, or constructing paths without normalization.

## AI-Assisted Code
- Annotate substantial AI-generated sections: `// AI-assisted: human-reviewed` (language appropriate comment syntax).
- Refine for clarity—AI output is a draft, not final code.

---
Last updated: 2025-08-14
