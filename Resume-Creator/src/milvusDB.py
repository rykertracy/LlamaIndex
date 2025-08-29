from llama_index.vector_stores.milvus import MilvusVectorStore

class MilvusDB():
    def __init__(self, db_name: str = "resume_db.db", dim: int = 768):
        self.db_name = db_name
        self.dim = dim

    def create_vector_store(self):
        vector_store = MilvusVectorStore(uri = "./" + self.db_name, dim = self.dim, overwrite = False)
        return vector_store

    def connect_vector_store(self):
        vector_store = MilvusVectorStore(uri = "./" + self.db_name, dim = self.dim, overwrite = False)
        return vector_store