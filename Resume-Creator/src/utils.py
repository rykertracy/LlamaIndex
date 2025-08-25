from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.vector_stores.postgres import PGVectorStore
import src.prompts as prompts

from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import src.prompts as prompts

# Initialize embedding model
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-base-en-v1.5",
    model_kwargs={"torch_dtype": "float16"},
    device="cuda",
    embed_batch_size=16,
    normalize=True,
    parallel_process=True,
    show_progress_bar=True
)

def fetch_all_resume_nodes(vector_store):
    """
    Query all resume nodes from the vector store.
    """
    query = VectorStoreQuery(query_embedding=None, mode="default", similarity_top_k=101)
    result = vector_store.query(query)
    return result.nodes

def aggregate_resume_text(nodes):
    """
    Combine all resume node contents into a single string.
    """
    return "\n\n".join(node.get_content(metadata_mode="all") for node in nodes)

def summarize_resumes(llm, resume_text):
    """
    Use LLM to summarize resume text using the prompt from prompts.py.
    """
    prompt = prompts.resume_prompt(resume_text)
    return llm.complete(prompt)