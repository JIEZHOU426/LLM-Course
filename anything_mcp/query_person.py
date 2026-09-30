import os
import urllib.request
import json

from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:3001/api/v1/workspace/46decf1f-7fe5-4d03-9584-9d2b6f2743a0/chat"
headers = {
    "Authorization": f"Bearer {os.getenv('ANYTHINGLLM_API_KEY', '')}",
    "Content-Type": "application/json"
}
payload = {
    "prompt": "钟金辉是一个什么人？请根据工作区中的文档详细介绍。",
    "searchTopK": 5,
    "searchScoreThreshold": 0.2
}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers=headers, method="POST")
try:
    resp = urllib.request.urlopen(req, timeout=30)
    result = resp.read().decode("utf-8")
    print(result)
except Exception as e:
    print(f"Error: {e}")
