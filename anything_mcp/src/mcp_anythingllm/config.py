from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    base_url: str = getenv("ANYTHINGLLM_BASE_URL", "http://localhost:3001")
    api_key: str = getenv("ANYTHINGLLM_API_KEY", "")
    host: str = getenv("MCP_HOST", "0.0.0.0")
    port: int = int(getenv("MCP_PORT", "8000"))


settings = Settings()
