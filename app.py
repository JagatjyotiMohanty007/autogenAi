import asyncio
import os

from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


async def main():
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    agent = AssistantAgent(
        name="AI_Assistant",
        model_client=model_client,
        system_message=(
            "You are a helpful AI software architect. "
            "Explain technical topics clearly and provide practical examples."
        ),
    )

    await Console(
        agent.run_stream(
            task="Explain Agentic AI architecture with a simple example."
        )
    )

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())