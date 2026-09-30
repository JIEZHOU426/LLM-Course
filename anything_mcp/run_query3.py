import subprocess, sys, time

proc = subprocess.Popen(
    [sys.executable, "-c", "import sys; sys.path.insert(0,r'src'); from mcp_anythingllm.server import mcp; import uvicorn; uvicorn.run(mcp.streamable_http_app, host='0.0.0.0', port=8001)"],
    cwd=r"D:\makeai\anything_mcp",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)
print(f"Server PID: {proc.pid}")
time.sleep(2)

import httpx, json
BASE = "http://localhost:8001/mcp"
headers = {"Content-Type": "application/json"}

# Call tool directly
r = httpx.post(BASE, json={"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"workspace_chat","arguments":{"workspace_slug":"default","question":"钟金辉是什么"}}}, headers=headers)
print("Raw response:", repr(r.text[:2000]))
print("Status:", r.status_code)

# Try SSE parse
if r.text.startswith("event:"):
    lines = r.text.strip().split("\n")
    for line in lines:
        if line.startswith("data: "):
            data = line[6:]
            print("Parsed:", json.dumps(json.loads(data), ensure_ascii=False, indent=2))

proc.terminate()
