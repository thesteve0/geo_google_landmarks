import db_query
import make_embeddings_query
from pathlib import Path

# image_path = Path("../query_image")

vector = make_embeddings_query.get_features()

querier = db_query.DBQuery()
querier.query_vector(vector)
for result in results:
    print("name : " + result.payload["picture"] + " :: score: " + str(result.score))

print("\n\n------------  Now a geo query in canada---\n\n")

querier.query_geo_vector(embedding=vector, country="CA")

print("finished")
