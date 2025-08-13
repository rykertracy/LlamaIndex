# Module to reduce repetitive code for loading environment variables
import os
from dotenv import load_dotenv
def load_env():
    """Load environment variables from a .env file located in the main directory."""
    dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path)
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print("API Key Loaded...")
    else:
        print("API KEY NOT FOUND...")
    return api_key