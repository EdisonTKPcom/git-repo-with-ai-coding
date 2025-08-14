# Refactor Extension (@refactor)

Focus when performing refactors:
- Preserve externally observable behavior & public APIs.
- Improve clarity: smaller functions, remove duplication.
- Keep or enhance test coverage; add missing edge cases.
- Avoid premature abstraction; remove dead code.
- Maintain performance characteristics unless improvement is intentional & measured.

Output Format Guidance:
- Provide diff-like suggestions or bullet steps.
- Highlight potential risks (side effects, global state, error handling changes).
