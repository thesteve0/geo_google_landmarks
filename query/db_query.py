import psycopg
from pgvector.psycopg import register_vector

# @todo this whole class needs to be rewritten
class DBQuery:

    def __init__(self):

        self.connect_string = f"host=localhost user=postgres password='letmein' dbname=geoimage"
        self.conn = psycopg.connect(self.connect_string, autocommit=True)

    # just a normal vector query
    def query_vector(self, vector):
        with self.conn.cursor() as cur:
            cur.execute(SQL)

        vector = vector[0]
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=20
        )
        return search_result

    # this one includes spatial
    # for the workshop we will hardcode the country to use
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
