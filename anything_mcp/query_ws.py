import os

import httpx
from dotenv import load_dotenv

load_dotenv()
headers = {"Authorization": f"Bearer {os.getenv('ANYTHINGLLM_API_KEY', '')}"}
try:
    r = httpx.get("http://localhost:3001/api/v1/workspaces", headers=headers)
    print(r.json())
except Exception as e:
    print(f"Error: {e}")
