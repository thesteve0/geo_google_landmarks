import psycopg
import numpy as np
from pgvector.psycopg import register_vector

# @todo this whole class needs to be rewritten
class DBQuery:

    def __init__(self):

        self.connect_string = f"host=localhost user=postgres password='letmein' dbname=geoimage"
        self.conn = psycopg.connect(self.connect_string, autocommit=True)
        register_vector(self.conn)


    # just a normal vector query
    def query_vector(self, embedding):
        new_embedding = embedding[0]
        with self.conn.cursor() as cur:
            results = cur.execute('SELECT id, (embedding <=> %s) as distance, filename, url '
                                  'FROM images ORDER BY embedding <=> %s LIMIT 10', (new_embedding, new_embedding, )).fetchall()

        for result in results:
            print("id: " + str(result[0]) + " || distance: " +  str(result[1]) + " || URL: " + str(result[3]))

    # this one includes spatial
    # for the workshop we will hardcode the country to use
    def query_geo_vector(self, embedding, country):
        vector = embedding[0]
        with self.conn.cursor() as cur:
            results = cur.execute('SELECT i.id, (i.embedding <=> %s) AS distance, i.filename,  i.url '
                                  'FROM images AS i, world AS w WHERE w.iso = %s AND ST_intersects(w.geog, i.location) '
                                  'ORDER BY embedding <=> %s LIMIT 10', (vector, country, vector, )).fetchall()

            for result in results:
                print("id: " + str(result[0]) + " || distance: " +  str(result[1]) + " || URL: " + str(result[3]))
