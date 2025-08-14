# /test_plan Command

Purpose: Generate or refine a structured test plan.

Output Sections:
1. Scope (features / functions under test)
2. In-Scope vs Out-of-Scope
3. Test Matrix (Case | Category | Preconditions | Steps | Expected)
4. Edge Cases & Negative Tests
5. Performance / Load Considerations (if applicable)
6. Security / Abuse Cases (injection, DoS, auth bypass)
7. Tooling / Automation Notes

Guidelines:
- Prefer concise tables or bullet lists.
- Identify missing coverage.
- Flag nondeterministic areas needing mocks.
