import subprocess, sys, time, os, signal

proc = subprocess.Popen(
    [sys.executable, "-c", "import sys; sys.path.insert(0,r'src'); from mcp_anythingllm.server import mcp; import uvicorn; uvicorn.run(mcp.streamable_http_app, host='0.0.0.0', port=8001)"],
    cwd=r"D:\makeai\anything_mcp",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)
print(f"Server PID: {proc.pid}")

import httpx, json
BASE = "http://localhost:8001/mcp"
headers = {"Content-Type": "application/json"}

# Initialize
r = httpx.post(BASE, json={"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}, headers=headers)
print("Init:", r.text)

# Get session ID from response
data = r.json()
sid = data.get("result", {}).get("sessionId")
print(f"Session ID: {sid}")

# Call tool
r2 = httpx.post(BASE, json={"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"workspace_chat","arguments":{"workspace_slug":"default","question":"钟金辉是什么"}}}, headers=headers)
print("Result:", r2.text)

proc.terminate()
