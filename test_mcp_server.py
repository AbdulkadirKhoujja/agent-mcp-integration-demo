import unittest
from unittest.mock import patch
import io
import json
from mcp_server import handle,invoke
class MCPTests(unittest.TestCase):
 def test_initialize(self):
  self.assertEqual(handle({"method":"initialize"})["serverInfo"]["name"],"portfolio-agent-mcp")
 def test_list(self):
  self.assertEqual(len(handle({"method":"tools/list"})["tools"]),2)
 def test_reject_write(self):
  self.assertTrue(handle({"method":"tools/call","params":{"name":"github.merge"}})["isError"])
 def test_validate_repo(self):
  with self.assertRaises(ValueError): invoke("github_issue_read",{"repo":"../../secret","number":1})
 def test_public_issue_mock(self):
  class Response:
   def __enter__(self): return io.BytesIO(json.dumps({"number":18,"title":"Example","state":"open","html_url":"https://github.com/example/repo/issues/18"}).encode())
   def __exit__(self,*args): pass
  with patch("mcp_server.urllib.request.urlopen",return_value=Response()):
   self.assertEqual(invoke("github_issue_read",{"repo":"example/repo","number":18})["number"],18)
 def test_run_tests(self):
  self.assertTrue(invoke("tests_run",{})["passed"])
