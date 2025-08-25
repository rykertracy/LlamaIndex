"""
PostgreSQL database management and vector store integration for LlamaIndex RAG pipeline.
"""
import psycopg2
from sqlalchemy import make_url
from llama_index.vector_stores.postgres import PGVectorStore

class DatabaseManager:
    def __init__(self, connection_string: str, db_name: str = "vector_db"):
        """
        Manage PostgreSQL database creation and deletion.
        Args:
            connection_string (str): PostgreSQL connection string.
            db_name (str): Name of the database.
        """
        self.connection_string = connection_string
        self.db_name = db_name
        self.conn = psycopg2.connect(self.connection_string)
        self.conn.autocommit = True

    def delete_database(self, db: str = None):
        """Delete the specified database if it exists."""
        db = db or self.db_name
        with self.conn.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {db}")

    def create_database(self):
        """Create the database, deleting it first if it exists."""
        self.delete_database()
        with self.conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {self.db_name}")

class VectorStoreManager:
    def __init__(self, connection_string: str, db_name: str = "vector_db"):
        self.connection_string = connection_string
        self.db_name = db_name

    def simple_connection(self, embed_dim: int = 768, table_name: str = "vector_store"):
        """Simple vector store connectionm"""
        url = make_url(self.connection_string)
        return PGVectorStore.from_params(
            database=self.db_name,
            host=url.host,
            password=url.password,
            port=url.port,
            user=url.username,
            table_name=table_name,
            embed_dim=embed_dim,
        )

    def create_index(self, embed_dim: int = 768, table_name: str = "vector_store"):
        """Create a vector store index with HNSW parameters."""
        url = make_url(self.connection_string)
        return PGVectorStore.from_params(
            database=self.db_name,
            host=url.host,
            password=url.password,
            port=url.port,
            user=url.username,
            table_name=table_name,
            embed_dim=embed_dim,
            hnsw_kwargs={
                "hnsw_m": 16,
                "hnsw_ef_construction": 64,
                "hnsw_ef_search": 40,
                "hnsw_dist_method": "vector_cosine_ops",
            }
        )
