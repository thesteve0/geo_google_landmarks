import psycopg
from pgvector.psycopg import register_vector


class DBUpload:
    DB_NAME= 'geoimage'

    def __init__(self, vector_size: int, table_name: str):

        self.vector_size = vector_size
        self.table_name = table_name
        conn = psycopg.connect("host=localhost user=postgres password='letmein'", autocommit=True)
        cursor = conn.cursor()

        cursor.execute("SELECT datname FROM pg_database;")

        list_database = cursor.fetchall()

        if (self.DB_NAME,) in list_database:
            cursor.execute(("DROP database "+ self.DB_NAME +" with (FORCE);"))
            cursor.execute("create database " + self.DB_NAME + ";")
        else:
            cursor.execute("create database " + self.DB_NAME + ";")

        #Now close the connection and switch DB
        conn.close()

        connect_string = f"host=localhost user=postgres password='letmein' dbname='{self.DB_NAME}'"

        conn = psycopg.connect(connect_string,  autocommit=True)
        conn.execute('CREATE EXTENSION IF NOT EXISTS vector')
        conn.execute('CREATE EXTENSION IF NOT EXISTS postgis')
        conn.close()

    def upsert_vectors(self, ids, vectors, payloads):
        connect_string = f"host=localhost user=postgres password='letmein' dbname='{self.DB_NAME}'"
        conn = psycopg.connect(connect_string, autocommit=True)
        register_vector(conn)

        conn.execute('DROP TABLE IF EXISTS %s' %  self.table_name)

        # ID is autogenerated and all the other columns besides embedding are in the payload
        conn.execute("""CREATE TABLE %s (id bigserial PRIMARY KEY, 
                            filename text, 
                            picture text,
                            url text,
                            location geography(POINT,4326) 
                            embedding vector(%s))""" % (self.table_name, self.vector_size,))

        # Copy in spatial data ST_Point(location["lon"), location["lat"])

        # create spatial and hnsw indices

        conn.commit()
        conn.close()

