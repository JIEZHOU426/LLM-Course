import httpx, json

BASE = "http://localhost:8001/mcp"
headers = {"Content-Type": "application/json"}

def call(method, params=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params:
        payload["params"] = params
    r = httpx.post(BASE, json=payload, headers=headers)
    return r.json()

# Initialize session
init = call("initialize", {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "test", "version": "1.0"}
})
print("Initialize:", json.dumps(init, ensure_ascii=False))

session_id = init.get("result", {}).get("sessionId")
if not session_id:
    # Try getting session info
    print("No sessionId in response, trying /messages")
    
# Call the tool
result = call("tools/call", {
    "name": "workspace_chat",
    "arguments": {"workspace_slug": "default", "question": "钟金辉是什么"}
})
print("Tool result:", json.dumps(result, ensure_ascii=False))
