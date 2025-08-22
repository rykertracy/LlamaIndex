"""
This module provides a class for creating and deleting PostgreSQL databases using psycopg2. It is specifically written for use with LlamaIndex in a RAG Pipeline. \
It connects to the server and allows database management tasks. 
"""
import psycopg2
from sqlalchemy import make_url
from llama_index.vector_stores.postgres import PGVectorStore
class CreateDB:
    def __init__(self, connection_string: str, db_name: str ="vector_db"):
        """A class for creating the database. Uses a connection string and database name.
        Args:
            connection_string (str): The connection string to PostgreSQL. Example: postgresql://postgres:password@localhost:5432
            db_name (str, optional): The name of the Vector Store. Defaults to "vector_db".
        """
        self.connection_string = connection_string
        self.db_name = db_name
        self.conn = psycopg2.connect(self.connection_string)
        self.conn.autocommit=True

    # Delete the PostgreSQL database.
    def delete_database(self, db: str=None):
        
        # use "vector_db" if db not specified.
        if db is None:
            db = self.db_name
        
        with self.conn.cursor() as c:
            c.execute(f"DROP DATABASE IF EXISTS {db}")
    
    # Create the PostgreSQL database, deleting it first if it already exists.
    def create_database(self):
        self.delete_database()
        with self.conn.cursor() as c:    
            c.execute(f"CREATE DATABASE {self.db_name}")

    # Add pgstore extension
    def pgstore_extension(self):
        pass
    #with self.conn.cursor() as c:

    
class Vector_Store:
    def __init__(self, connection_string: str, db_name: str = "vector_db"):
        self.connection_string = connection_string
        self.db_name = db_name

    def create_index(self):
        url = make_url(self.connection_string)
        vector_store = PGVectorStore.from_params(
            database=self.db_name,
            host=url.host,
            password=url.password,
            port=url.port,
            user=url.username,
            table_name="vector_store",
            embed_dim=768,  # Adjust based on your embedding model
            hnsw_kwargs={
                "hnsw_m": 16,
                "hnsw_ef_construction": 64,
                "hnsw_ef_search": 40,
                "hnsw_dist_method": "vector_cosine_ops",
            }
        )
        return vector_store
