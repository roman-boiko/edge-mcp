from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(
    "uv",
    args=[
        "--directory",
        "/Users/romanboiko/projects/edge-mcp/server",
        "run",
        "sensehatmcp.py",
    ],
)


ollama_model = OpenAIModel(
    model_name="llama3.2:1b",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
)

agent = Agent(ollama_model, mcp_servers=[server])


async def main():
    async with agent.run_mcp_servers():
        while True:
            user_input = input("Enter your prompt (or type 'exit' to quit): ")
            if user_input.strip().lower() == "exit":
                break
            result = await agent.run(user_input)
            print(result.output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
