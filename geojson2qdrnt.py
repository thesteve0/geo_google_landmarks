import json

import geojson

# This only accepts simple polygons NOT multipolygons
# This should actually have 2 methods
# 1 that returns the JSON needed a REST call
# 2 one that returns a valid GeoPolygon
# Maybe they are just static methods on the class and accept a JSON object as input



def geoJSON2coord_list(geojson_input: geojson):
    coord_array = geojson_input["geometry"]["coordinates"][0]
    result_array = []
    for coord_pair in coord_array:
        coord_obj = {"lon": coord_pair[0], "lat": coord_pair[1]}
        result_array.append(coord_obj)
    return result_array


def geoJSON_string2qjson(geojson_input: geojson):

    coord_array = geoJSON2coord_list((geojson_input))
    poly_filter = {"filter": {"must": [{"geo_polygon": {"exterior": {"points": coord_array}}}]}}
    return json.dumps(poly_filter)
    print("should be done")


def geoJSON_string2qgeom(geojson_input: geojson):
    print("not yet")

if __name__ == '__main__':
    with open("../germany.geojson", "r", encoding='utf_8') as content:
        print(geoJSON_string2qjson(json.load(content)))



# "geo_polygon": {
#     "exterior": {
#         "points": [
#             { "lon": -70.0, "lat": -70.0 },
#             { "lon": 60.0, "lat": -70.0 },
#             { "lon": 60.0, "lat": 60.0 },
#             { "lon": -70.0, "lat": 60.0 },
#             { "lon": -70.0, "lat": -70.0 }
#         ]
#     },
#     "interiors": [
#         {
#             "points": [
#                 { "lon": -65.0, "lat": -65.0 },
#                 { "lon": 0.0, "lat": -65.0 },
#                 { "lon": 0.0, "lat": 0.0 },
#                 { "lon": -65.0, "lat": 0.0 },
#                 { "lon": -65.0, "lat": -65.0 }
#             ]
#         }
#     ]
# }


# models.FieldCondition(
#     key="location",
#     geo_polygon=models.GeoPolygon(
#         exterior=models.GeoLineString(
#             points=[
#                 models.GeoPoint(
#                     lon=-70.0,
#                     lat=-70.0,
#                 ),
#                 models.GeoPoint(
#                     lon=60.0,
#                     lat=-70.0,
#                 ),
#                 models.GeoPoint(
#                     lon=60.0,
#                     lat=60.0,
#                 ),
#                 models.GeoPoint(
#                     lon=-70.0,
#                     lat=60.0,
#                 ),
#                 models.GeoPoint(
#                     lon=-70.0,
#                     lat=-70.0,
#                 )
#             ]
#         ),
#         interiors=[
#             models.GeoLineString(
#                 points=[
#                     models.GeoPoint(
#                         lon=-65.0,
#                         lat=-65.0,
#                     ),
#                     models.GeoPoint(
#                         lon=0.0,
#                         lat=-65.0,
#                     ),
#                     models.GeoPoint(
#                         lon=0.0,
#                         lat=0.0,
#                     ),
#                     models.GeoPoint(
#                         lon=-65.0,
#                         lat=0.0,
#                     ),
#                     models.GeoPoint(
#                         lon=-65.0,
#                         lat=-65.0,
#                     )
#                 ]
#             )
#         ]
#     )
# )