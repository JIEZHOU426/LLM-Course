import subprocess, sys, time, os, signal

proc = subprocess.Popen(
    [sys.executable, "-c", "import sys; sys.path.insert(0,r'src'); from mcp_anythingllm.server import mcp; import uvicorn; uvicorn.run(mcp.streamable_http_app, host='0.0.0.0', port=8001)"],
    cwd=r"D:\makeai\anything_mcp",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)
print(f"Server PID: {proc.pid}")
time.sleep(2)

from mcp.client.streamable_http import streamablehttp_client
import asyncio, json

async def main():
    async with streamablehttp_client("http://localhost:8001/mcp") as client:
        result = await client.call_tool("workspace_chat", {"workspace_slug": "default", "question": "钟金辉是什么"})
        print(json.dumps(result, ensure_ascii=False, indent=2))

asyncio.run(main())
proc.terminate()
