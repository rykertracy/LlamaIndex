'''
Using Chat Context, following the example in: https://docs.llamaindex.ai/en/stable/getting_started/starter_example
'''

### Using an AgentWorkflow to remember chat context
import loadEnv
loadEnv.load_env()

import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from llama_index.llms.openai import OpenAI

# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    tools=[multiply],
    llm=OpenAI(model="gpt-5-nano-2025-08-07"),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)

ctx = Context(agent)

async def main():
    # Run the agent
    response = await agent.run("My name is Ryker", ctx=ctx)
    response = await agent.run("What is my name?", ctx=ctx)
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())

'''
Comments: Output was
Your name is Ryker. If you'd like, tell me two numbers to mulitply or a math expression to evaluate.

Cool that it took its system prompt to heart.

Additionally, I had the tools argument of the FunctionAgent commented. It appears even if that is not present the FunctionAgent will still work.
'''
