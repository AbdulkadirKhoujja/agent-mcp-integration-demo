"""Synthetic agent-tool integration example; no network or real MCP transport."""
from dataclasses import dataclass, field

@dataclass
class Gateway:
    permissions: set = field(default_factory=lambda: {'issue.read', 'tests.run'})
    audit: list = field(default_factory=list)

    def invoke(self, tool, arguments=None):
        arguments = arguments or {}
        if tool not in self.permissions:
            result = {'ok': False, 'error': 'permission_denied'}
        elif tool == 'issue.read':
            result = {'ok': True, 'issue': {'id': str(arguments.get('id', 'DEMO-1')), 'state': 'open'}}
        elif tool == 'tests.run':
            result = {'ok': True, 'checks': ['lint', 'unit', 'policy'], 'passed': 3}
        else:
            result = {'ok': False, 'error': 'unsupported_tool'}
        self.audit.append({'tool': tool, 'allowed': result['ok']})
        return result

if __name__ == '__main__':
    g = Gateway()
    for name in ('issue.read', 'tests.run', 'github.merge'):
        print(name, g.invoke(name, {'id': 18}))
    print('audit', g.audit)
