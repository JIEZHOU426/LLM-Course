import httpx, json

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "workspace_chat",
        "arguments": {
            "workspace_slug": "default",
            "question": "钟金辉是什么"
        }
    }
}
r = httpx.post("http://localhost:8001/mcp", json=payload, headers={"Content-Type": "application/json"})
print(r.text)
