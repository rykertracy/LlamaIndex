'''
A combination of the calculator agent and chat-history agent examples, plus a few more capabilities. https://docs.llamaindex.ai/en/stable/getting_started/starter_example

This script includes foundational RAG functionality.
'''
# ---------- Imports ----------
# Load API Key with user-defined script
import loadEnv
loadEnv.load_env()

# Import necessary LlamaIndex modules
import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

# Add vector storage for RAG
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# ---------- Load Data ----------
documents = SimpleDirectoryReader('data').load_data() # This directory contains a simple text file with some text.
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine() 

# ---------- Define Agent and Funcitons ----------
def multiply(a: float, b: float) -> float: # Defining input data type and output data type.
    ''' Multiply two numbers '''
    return a * b

async def search_documents(query: str) -> str:
    ''' Answering natural language questions about an essay'''
    response = await query_engine.aquery(query)
    return str(response)

agent = FunctionAgent(
    tools = [multiply, search_documents],
    llm = OpenAI(model="gpt-5-nano-2025-08-07"),
    system_prompt="You are a helpful assistant that can search documents and perform mathematical calculations.",
)

async def main():
    response = await agent.run(
        "What did the author do in college? Also, what's 7 * 8?"
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())