import asyncio
import sys

sys.path.insert(0, r"D:\makeai\chongwu_mcp\src")

from mcp import ClientSession, StdioServerParameters, stdio_client


async def main():
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "pet_hospital_mcp"],
        cwd=r"D:\makeai\chongwu_mcp\src",
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("== MCP 已注册工具 ==")
            for t in tools.tools:
                print(f"- {t.name}")

            print()
            print("== get_pets (species=犬, pageSize=1) ==")
            result = await session.call_tool("get_pets", {"species": "犬", "pageSize": 1})
            for c in result.content:
                print(c.text)

            print()
            print("== 边界: get_pets 无参数 ==")
            result = await session.call_tool("get_pets", {})
            for c in result.content:
                print("返回:", str(c))
            print("MCP is_error:", result.is_error)

            print()
            print("== 边界: add_pet 缺必填参数 ==")
            result = await session.call_tool("add_pet", {"name": "x"})
            for c in result.content:
                print("返回:", str(c)[:200])
            print("MCP is_error:", result.is_error)


asyncio.run(main())