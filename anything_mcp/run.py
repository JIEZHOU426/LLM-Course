import sys
sys.path.insert(0, r"D:\makeai\anything_mcp\src")
from mcp_anythingllm.server import mcp

if __name__ == "__main__":
    import uvicorn
    app = mcp.streamable_http_app
    uvicorn.run(app, host="0.0.0.0", port=8000)
