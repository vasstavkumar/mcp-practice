from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import starlette


async def main():

    command = "python3" 
    server_params = StdioServerParameters(
        command=command,
        args=['/Users/vasstavkumarchava/Desktop/mcp-new/server/server.py'],
    )
    
        

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            tools = tools_result.tools
            print(tools)

if __name__ == "__main__":
    asyncio.run(main())