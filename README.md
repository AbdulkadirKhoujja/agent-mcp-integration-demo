# Agent MCP Integration Demo

**Real local MCP JSON-RPC stdio server** implementing initialize, tools/list, and tools/call. Includes a read-only public GitHub issue tool using the GitHub REST API, a local test-runner tool, deny-by-default dispatch, validation, and structured audit events on stderr. No credentials required for public issue reads.

This is an original pre-contract portfolio demo, not client work. The public GitHub endpoint is real when internet access is available; unit tests mock the endpoint for repeatability. No GitHub write, Jira, or hosted deployment is claimed.

## Run
```bash
python -m unittest discover -s . -p 'test_*.py' -v
python mcp_server.py
```
Send newline-delimited JSON to stdin:
```json
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"demo","version":"1"}}}
{"jsonrpc":"2.0","id":2,"method":"tools/list"}
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"github_issue_read","arguments":{"repo":"python/cpython","number":1}}}
{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"github.merge","arguments":{}}}
```

## Security boundaries
No shell command arguments are accepted. Test execution runs only the repository's own fixed unittest command. GitHub issue access is read-only, public, and validated; responses may be rate limited by GitHub. Audit events are local process logs, not durable storage. The protocol demo uses line-delimited JSON framing and does not claim compatibility with every MCP client transport; a production implementation should use the official MCP SDK, durable audit storage, authentication, and deployment-specific authorization.
