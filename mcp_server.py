"""Minimal MCP JSON-RPC 2.0 stdio server with safe public GitHub reads."""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

TOOLS = [
 {"name":"github_issue_read","description":"Read a public GitHub issue (read only).","inputSchema":{"type":"object","properties":{"repo":{"type":"string"},"number":{"type":"integer","minimum":1}},"required":["repo","number"]}},
 {"name":"tests_run","description":"Run the repository's own unit tests.","inputSchema":{"type":"object","properties":{}}}
]
AUDIT = []
def invoke(name, args):
    if name == "github_issue_read":
        repo, number = args.get("repo",""), args.get("number")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",repo) or type(number) is not int or number < 1:
            raise ValueError("Invalid repository or issue number")
        url = f"https://api.github.com/repos/{repo}/issues/{number}"
        req = urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"portfolio-mcp-demo"})
        with urllib.request.urlopen(req, timeout=8) as response:
            obj = json.load(response)
        return {"number":obj["number"],"title":obj["title"],"state":obj["state"],"url":obj["html_url"]}
    if name == "tests_run":
        import subprocess
        result = subprocess.run([sys.executable,"-m","unittest","discover","-s",".","-p","test_*.py"],cwd=os.path.dirname(__file__),capture_output=True,text=True,timeout=20)
        return {"passed":result.returncode==0,"output":(result.stdout+result.stderr)[-2000:]}
    raise ValueError("Tool not permitted")
def handle(request):
    method=request.get("method")
    if method=="initialize":
        return {"protocolVersion":"2025-03-26","capabilities":{"tools":{}},"serverInfo":{"name":"portfolio-agent-mcp","version":"0.2.0"}}
    if method=="notifications/initialized": return None
    if method=="ping": return {}
    if method=="tools/list": return {"tools":TOOLS}
    if method=="tools/call":
        params=request.get("params") or {}
        name=params.get("name","")
        try:
            result=invoke(name,params.get("arguments") or {})
            success=True
            payload={"content":[{"type":"text","text":json.dumps(result)}],"isError":False}
        except Exception as exc:
            success=False
            payload={"content":[{"type":"text","text":str(exc)}],"isError":True}
        AUDIT.append({"at":datetime.now(timezone.utc).isoformat(),"tool":name,"ok":success})
        print(json.dumps({"audit":AUDIT[-1]}),file=sys.stderr,flush=True)
        return payload
    raise ValueError("Unknown method")
def main():
    for line in sys.stdin:
        try:
            req=json.loads(line)
            result=handle(req)
            if "id" in req and result is not None:
                print(json.dumps({"jsonrpc":"2.0","id":req["id"],"result":result}),flush=True)
        except Exception as exc:
            print(json.dumps({"jsonrpc":"2.0","id":req.get("id") if isinstance(req,dict) else None,"error":{"code":-32603,"message":str(exc)}}),flush=True)
if __name__=="__main__": main()
