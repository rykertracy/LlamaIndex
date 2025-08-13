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

# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    llm=OpenAI(model="gpt-5-nano-2025-08-07"),
    system_prompt="You are a helpful assistant.",
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
Your name is Ryker. I can continue to use it in our replies if you’d like. How can I assist you today, Ryker?
'''
