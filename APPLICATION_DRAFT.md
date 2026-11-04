# Upwork application package (draft; not submitted)

**Job:** MCP Server Developer for AI Coding Agents

**Proposed rate:** $35/hour, within the listed $30–50/hour range.

## Proposal
Hello,

I build Python-based agent orchestration and tool integrations, including the Orchestryn project. Your emphasis on reliable MCP tools, GitHub and issue-tracker access, permission boundaries, and auditable agent actions matches my work.

For a focused demonstration I created a Python MCP-style JSON-RPC server that discovers tools, reads public GitHub issues, runs a fixed local test command, rejects unauthorized actions, and emits audit events. It is explicitly a portfolio demonstration, not a deployed production system.

Repositories:
- https://github.com/AbdulkadirKhoujja/agent-mcp-integration-demo
- https://github.com/AbdulkadirKhoujja/Orchestryn

I would start by identifying your existing agent runtime and MCP transport, then implement a small set of typed, least-privilege integrations with tests, bounded timeouts and an auditable execution trail.

Best regards,
Abdul

## Screening question 1
I built agent tool integrations in Orchestryn, a supervised agent infrastructure project, and a separate Python MCP-style demonstration. The demonstration lets an agent discover tools, read public GitHub issues, run a fixed local test suite and receive explicit denial for unauthorized write operations. Orchestryn is the broader existing project; the demo is a smaller illustrative implementation. The demo has no production deployment or GitHub write capability.

## Screening question 2
https://github.com/AbdulkadirKhoujja

**Before submission:** Verify repository tests and demo commands. Do not claim an unverified CI result.
