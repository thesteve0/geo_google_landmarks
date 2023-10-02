from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


class DBUpload:

    def __init__(self, vector_size: int, collection_name: str):

        self.client = QdrantClient(host="localhost", port=6333)

        self.vector_size = vector_size
        self.collection_name = collection_name

        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )

    def upsert_vectors(self, ids, vectors, payloads):
        self.client.upload_collection(
            collection_name=self.collection_name,
            ids=ids,
            vectors=vectors,
            payload=payloads
        )

    def query_vector(self, vector):
        print(type(vector))
        vector = vector[0]
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=5

        )
        return search_result
