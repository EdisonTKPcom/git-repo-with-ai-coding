# /risk_review Command

Purpose: Structured security / risk analysis for a proposed change.

Output Sections:
1. Summary
2. Changed Surfaces (files, endpoints, boundaries)
3. Threat Enumeration (table: Threat | Vector | Impact | Likelihood | Mitigation)
4. Input & Output Validation Gaps
5. Dependency / Supply Chain Considerations
6. Secrets & Sensitive Data Handling
7. Logging & Observability
8. Residual Risks & Follow-ups

Guidelines:
- Prioritize exploitable, realistic threats.
- Avoid speculative micro-optimizations as risks.
- Call out need for additional tests or fuzzing.
