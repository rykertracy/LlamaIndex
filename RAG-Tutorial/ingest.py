import torch
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from pgstore import CreateDB, Vector_Store


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

# Set the embedding model in the global settings
Settings.embed_model = embed_model
### ------------------------------------


### ---------- PostgreSQL Database Connection ----------
# Create the database connection
connection_string = "postgresql://postgres:123456@localhost:5432"
db = CreateDB(connection_string)
db.create_database()

# Create the vector store and index it based on the test doc.
vs = Vector_Store(connection_string, db_name="vector_db")
vector_store = vs.create_index()
### ------------------------------------


### ---------- Ingest Documents ----------
# Read the documents from the directory
documents = SimpleDirectoryReader("./documents/test").load_data(show_progress=True)
print("Documents ID:", documents[0].doc_id)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
    storage_context=storage_context,
    show_progress=True
)
### -------------------------------------