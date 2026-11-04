# Demonstration recording script (approximately 75 seconds)

**Disclosure:** This is a guided demonstration of a portfolio project, not footage of client delivery.

1. Show repository README and `mcp_server.py`. Explain JSON-RPC MCP-style initialize and tool discovery.
2. Run `python -m unittest discover -s . -p 'test_*.py' -v`. Show actual results; do not claim passing until verified.
3. Run `python mcp_server.py` and send initialize and tools/list requests from README.
4. Request a public GitHub issue; show the returned issue title and URL, noting GitHub network access is required.
5. Attempt `github.merge`; show denial and audit event.
6. Close with the security boundaries: no write access, no credentials, no durable audit store, not a deployed production service.

Suggested narration: “This is a deliberately restricted MCP-style agent integration. It exposes discovery and read-only issue retrieval, plus a fixed local test command. An unauthorized merge request is rejected before any external action. Audit events record the attempted operation. The production Orchestryn project is separate; this demo isolates the controls relevant to the client's brief.”
