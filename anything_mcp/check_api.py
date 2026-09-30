import sys, json
sys.path.insert(0, r'D:\makeai\anything_mcp\src')
import asyncio, httpx
from mcp_anythingllm.config import settings

async def main():
    headers = {
        'Authorization': f'Bearer {settings.api_key}',
        'Content-Type': 'application/json',
    }
    async with httpx.AsyncClient() as client:
        # Try various endpoints
        endpoints = [
            '/api/v1/workspaces',
            f"/api/v1/workspaces/46decf1f-7fe5-4d03-9584-9d2b6f2743a0",
            '/api/v1/app/document/workspace/46decf1f-7fe5-4d03-9584-9d2b6f2743a0',
            '/api/v1/workspace/46decf1f-7fe5-4d03-9584-9d2b6f2743a0',
        ]
        for ep in endpoints:
            try:
                url = settings.base_url.rstrip('/') + ep
                resp = await client.get(url, headers=headers)
                text = resp.text[:600]
                print(f"{ep}: {resp.status_code} - {text}")
            except Exception as e:
                print(f"{ep}: Error - {e}")
    await client.aclose()

asyncio.run(main())
