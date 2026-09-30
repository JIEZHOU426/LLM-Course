import mcp
print("mcp version:", mcp.__version__)
try:
    from mcp.client.streamable_http import streamablehttp_client
    print("streamablehttp_client available")
except ImportError as e:
    print(f"streamablehttp_client import error: {e}")
try:
    from mcp.client import StreamableHttpClient
    print("StreamableHttpClient available")
except ImportError as e:
    print(f"StreamableHttpClient import error: {e}")

import pkgutil, mcp
for importer, modname, ispkg in pkgutil.walk_packages(mcp.__path__, mcp.__name__ + '.'):
    print(modname)
