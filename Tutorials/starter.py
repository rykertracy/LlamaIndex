'''
A basic agent example from: https://docs.llamaindex.ai/en/stable/getting_started/starter_example
'''

# Load API key from .env file in main directory
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)
api_key = os.getenv('OPENAI_API_KEY')
print("API Key loaded:", bool(api_key)) # This will print True if the key is loaded successfully

# ------------------------- Calculator Agent Example -------------------------
import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

# Simple calculator function
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# Create an agent workflow with the calculator function
agent = FunctionAgent(
    tools=[multiply],
    llm=OpenAI(model="gpt-5-nano-2025-08-07"),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)

async def main():
    # Run the agent
    response = await agent.run("What is 300 * 50?")
    print(str(response))

if __name__ == "__main__":
    asyncio.run(main())