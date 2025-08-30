"""
Storing data into milvus and accessing that data.
"""
# Vector Store
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

# Storage embeddings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

#Env reader
import dotenv

class VectorStoreManage():

    def __init__(self, db_name: str = "resume_db"):
        self.db_name = db_name

    def hugging_embed_model(self, model_name: str="BAAI/bge-base-en-v1.5", 
                            model_kwargs: dict ={"torch_dtype": "float16"}, device: str="cuda", embed_batch_size: int=16,
                            normalize: bool=True, parellel_process: bool=True, show_progress_bar: bool=True):
        """Initialize the HuggingFace Embeddings model. This is the preferred embeddings model because it's a decent model and it's free.

        Args:
            model_name (str, optional): Embedding model name. Defaults to "BAAI/bge-base-en-v1.5".
            model_kwargs (_type_, optional): Standard embedding model keyword arguments. Defaults to {"torch_dtype": "float16"}.
            device (str, optional): CPU or GPU (cuda). Defaults to "cuda".
            embed_batch_size (int, optional): Ingestion batch size into CPU or GPU. Defaults to 16.
            normalize (bool, optional): Normalize the embeddings. Defaults to True.
            parellel_process (bool, optional): Parellel process the embeddings. Defaults to True.
            show_progress_bar (bool, optional): Display a progress bar. Defaults to True.

        Returns:
            Embedding Model: Default huggingface embedding model base-en-v1.5
        """
        return HuggingFaceEmbedding(model_name=model_name, model_kwags=model_kwargs, device=device, embed_batch_size=embed_batch_size, normalize=normalize, parellel_process=parellel_process, show_progress_bar=show_progress_bar)
    
