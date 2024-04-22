import db_query
import make_embeddings_query
from pathlib import Path

# image_path = Path("../query_image")

vector = make_embeddings_query.get_features()

db_query.DBQuery(vector)
# results = query.query_vector(vector)
# for result in results:
#     print("name : " + result.payload["picture"] + " :: score: " + str(result.score))

print("\n\n------------  Now a geo query centered in Pennsylvania with a 1000 km radius---\n\n")

results = query.query_geo_vector(vector)
for result in results:
    print("name : " + result.payload["picture"] + " :: score: " + str(result.score) + " :: " + result.payload["url"])

print("finished")
