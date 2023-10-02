from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


class DBQuery:

    def __init__(self, vector_size: int, collection_name: str):

        self.client = QdrantClient(host="localhost", port=6333)

        self.vector_size = vector_size
        self.collection_name = collection_name

    def query_vector(self, vector):
        vector = vector[0]
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=20
        )
        return search_result
