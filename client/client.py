from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import starlette


async def main():

    server_params = StdioServerParameters(
        command =  "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3",
        args=[
            "--directory",
            "/Users/vasstavkumarchava/Desktop/mcp-new/server",
            "run",
            "server.py"
        ]
    )
        

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            tools = tools_result.tools
            print(tools)

if __name__ == "__main__":
    asyncio.run(main())