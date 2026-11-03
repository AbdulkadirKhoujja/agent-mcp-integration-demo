import unittest
from demo import Gateway

class GatewayTests(unittest.TestCase):
    def test_issue(self):
        self.assertEqual(Gateway().invoke('issue.read', {'id': 18})['issue']['id'], '18')
    def test_tests(self):
        self.assertEqual(Gateway().invoke('tests.run')['passed'], 3)
    def test_denied_write(self):
        self.assertEqual(Gateway().invoke('github.merge')['error'], 'permission_denied')
    def test_audit(self):
        g = Gateway(); g.invoke('github.merge')
        self.assertEqual(g.audit, [{'tool': 'github.merge', 'allowed': False}])
