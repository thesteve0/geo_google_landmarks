from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import models


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

    def query_geo_vector(self, vector):
        vector = vector[0]
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=20,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                    key="location",
                    geo_radius=models.GeoRadius(
                        center=models.GeoPoint(
                            lat=41.417733,
                            lon=-77.473338,
                        ),
                        radius=1000000.0,
                    ),
                )
                ]
            )
        )
        return search_result
