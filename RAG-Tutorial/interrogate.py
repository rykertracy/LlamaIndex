from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from pgstore import CreateDB, Vector_Store
import torch
import os
# Load API Key with user-defined script
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)
api_key = os.getenv('OPENAI_API_KEY')

### ---------- Embedding Model ----------
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-base-en-v1.5",
    model_kwargs={
        "torch_dtype": "float16"
        },
    device="cuda" if torch.cuda.is_available() else "cpu",
    embed_batch_size=16,
    normalize=True,
    show_progress_bar=True
)

# Set the embedding model in teh global settings
Settings.embed_model = embed_model


vs = Vector_Store(
    connection_string="postgresql://postgres:123456@localhost:5432",
    db_name="vector_db")
vector_store = vs.create_index()

### Query the docs
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, show_progress=True)
query_engine = index.as_query_engine()

response = query_engine.query("List 3 scientific methodologies that are used in this paper.")
print(response)