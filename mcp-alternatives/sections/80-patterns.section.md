## Design Patterns for Agent-Friendly CLIs

When building or choosing CLI tools for LLM agents:

1. **`usage` or `--help` command** — Self-documenting for agents
2. **JSON output** — Composable with `jq`, `yq`
3. **Focused scope** — 3-5 core operations, not 20+
4. **Smart ID resolution** — Accept natural formats (e.g., `ABC-123`)
5. **Exit codes** — Clear success/failure for scripting
6. **Streaming support** — Don't buffer huge responses

See [CLI/SDK Over Context Bloat](cli-sdk-over-context-bloat.md) for detailed patterns.

---
