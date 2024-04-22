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
            results = cur.execute('SELECT id, (embedding <=> %s) as distance, abstract '
                                   'FROM images ORDER BY embedding <=> %s LIMIT 10', (vector, vector, )).fetchall()

        for result in results:
            print("id: " + str(result[0]) + " || distance: " +  str(result[1]) + " || abstract: " + result[2][:50])

    # this one includes spatial
    # for the workshop we will hardcode the country to use
    def query_geo_vector(self, vector, country):
        with self.conn.cursor() as cur:
            results = cur.execute('SELECT id, (embedding <=> %s) as distance, abstract '
                                  'FROM images ORDER BY embedding <=> %s LIMIT 10', (vector, vector, )).fetchall()


            for result in results:
                print("id: " + str(result[0]) + " || distance: " +  str(result[1]) + " || abstract: " + result[2][:50])
            return search_result
