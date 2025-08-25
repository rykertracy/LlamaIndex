
# Script for summarizing resume data using LLM and vector store retrieval
# Imports utility functions, database manager, and loads environment variables
from src import utils
from src.postgresDB import pgstore
from dotenv import load_dotenv
import os
from llama_index.llms.openai import OpenAI


class SummarizeResumes():
    """
    Summarizes resume data from a PostgreSQL vector store using an LLM.
    Requirements:
      - PostgreSQL database 'resume_db' with table 'resume_table'.
      - .env file containing 'OPENAI_API_KEY' and 'connection_string'.
    """
    def __init__(self, dotenv_path: str = "c:\LlamaIndex\.env", llm_model: str ="gpt-5-mini-2025-08-07", llm_temp: float = 0.5):
        # Load environment variables from .env file
        load_dotenv(dotenv_path)

        # Check for OpenAI API key
        if os.getenv("OPENAI_API_KEY") is not None:
            print("Successfully Loaded OpenAI API Key...")
            self.api_key = os.getenv("OPENAI_API_KEY")
        else:
            raise KeyError("No API Key (in .env) Loaded")

        # Check for PostgreSQL connection string
        if os.getenv("connection_string") is not None:
            print("Successfully Loaded PostgreSQL Connection String...")
        else:
            raise KeyError("PostgreSQL Connection String (in .env) Empty")

        self.connection_string = os.getenv("connection_string")
        # Initialize LLM with specified model and temperature
        self.llm = OpenAI(model=llm_model, temperature=llm_temp)
        # Connect to vector store and resume table
        self.vs = pgstore.VectorStoreManager(connection_string=self.connection_string, db_name='resume_db').simple_connection(table_name="resume_table")

    def _compile_nodes(self):
        """Fetch all resume nodes from the vector store."""
        nodes = utils.fetch_all_resume_nodes(self.vs)
        print("Nodes compiled...")
        return nodes

    def _compile_resume_text(self):
        """Aggregate all resume node text into a single string."""
        nodes = self._compile_nodes()
        resume_text = utils.aggregate_resume_text(nodes)
        print("Text compiled...")
        return resume_text

    def cv_summary(self):
        """Summarize the aggregated resume text using the LLM."""
        resume_text = self._compile_resume_text()
        print("Summarizing...")
        cv_summary = utils.summarize_resumes(self.llm, resume_text)
        return cv_summary

# Run summarization if script is executed directly
if __name__ == "__main__":
    summarizer = SummarizeResumes()
    print(summarizer.cv_summary())