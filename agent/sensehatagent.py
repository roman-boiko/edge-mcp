import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.mcp import MCPServerStdio
import yaml

with open("agent/sensehatagent_config.yaml", "r") as f:
    config = yaml.safe_load(f)
    sensehat_agent_config = config["agent"]
    sensehat_agent_command = sensehat_agent_config["command"]
    sensehat_agent_args = sensehat_agent_config["args"]

server = MCPServerStdio(
    command=sensehat_agent_command,
    args=sensehat_agent_args,
)


ollama_model = OpenAIModel(
    model_name="llama3.2",
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
    asyncio.run(main())
