import subprocess, sys, time, os
sys.path.insert(0, r"D:\makeai\anything_mcp\src")
from mcp_anythingllm.server import mcp
import uvicorn
app = mcp.streamable_http_app
proc = subprocess.Popen([sys.executable, "-c", f"from mcp_anythingllm.server import mcp; import uvicorn; uvicorn.run(mcp.streamable_http_app, host='0.0.0.0', port=8001)"], cwd=r"D:\makeai\anything_mcp")
time.sleep(2)
print(f"Server PID: {proc.pid}")
print("Server should be running on port 8001")
