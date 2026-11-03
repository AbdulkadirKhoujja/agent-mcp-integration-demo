# Agent MCP Integration Demo

Original, synthetic pre-contract portfolio demonstration. This repository illustrates MCP-style tool dispatch, least-privilege permissions, simulated issue retrieval, test execution, and audit events. It is **not** a production MCP server and does not connect to GitHub or Jira. No client materials or secrets are used.

Run `python -m unittest discover -s . -v` and `python demo.py`.

For production use, replace mocks with authenticated adapters, add a real MCP transport, secret management, input validation, persistent audit storage, and integration tests.
