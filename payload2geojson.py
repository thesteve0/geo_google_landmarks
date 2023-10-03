# >>> Feature(geometry=my_point, id=27)  # doctest: +ELLIPSIS
# {"geometry": {"coordinates": [-3.68..., 40.4...], "type": "Point"}, "id": 27, "properties": {}, "type": "Feature"}
import json
from decimal import Decimal

import geojson
from geojson import Feature, Point
from qdrant_client.conversions.conversion import payload_to_grpc

geojson_array = []


# Load the payload JSON
with open("D:\data\google-landmarks\geo-google-landmark-payload.json") as jf:
    input_json = json.load(jf)

    # Now iterate through and make an array of features
    for id, payload in input_json.items():
        lon = float(payload["location"]["lon"])
        lat = float(payload["location"]["lat"])
        my_point = Point((lon, lat))
        geojson_array.append(Feature(geometry=my_point, id=payload["picture"], properties={"url": payload["url"]}))

with open("D:\data\google-landmarks\geo-google-landmark.geojson", "w") as output:
    geojson.dump(geojson_array, fp=output)

print("finished")
