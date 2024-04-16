import requests
from bs4 import BeautifulSoup

from csv import DictReader
from pathlib import Path
import re
import uuid
import json

import db_upload
import make_embeddings_upload

#TODO this is definitely not efficient as it generates vectors for all the images, not just the ones with geo
# to fix we would somehow copy all the original images in the payloads_non_list into the directory we want to use in the vector making

#TODO there is also repeated code everywhere
# And hard coded values for too many things

image_path = Path("images_000")

my_file = Path('train_attribution_geo.json')
payloads_non_list = {}
if my_file.is_file():
    # file already exists
    with open('train_attribution_geo.json') as incoming_json:
        payloads_non_list = json.load(incoming_json)
    print("We already have metadata load the data into python non-list")
else:
    metadata_path = "train_attribution.csv"
    image_names = {}

    for path in image_path.rglob('*.*'):
        match = re.search('.*(\w{16})\.jpg$', str(path))
        image_names[match.group(1)] = path

    csvfile = open(metadata_path, "r", encoding='utf-8')
    csvlines = DictReader(csvfile)


    i = 1
    for line in csvlines:
        if line['id'] in image_names:
            try:
                page = requests.get(line['url'])
                html = BeautifulSoup(page.text, features="html.parser")
                our_tag = html.find('a', {"data-style": "osm-intl"})
                if our_tag is not None:
                    if "data-lat" in our_tag.attrs and "data-lon" in our_tag.attrs:
                        lat = float(our_tag.attrs["data-lat"])
                        lon = float(our_tag.attrs["data-lon"])
                    # We have our payload at this point
                        print("found one " + line['id'] + " : " + line['url'] + " coords: " + str(lat) + ", " + str(lon))
                        payloads_non_list[line['id']] = {"picture": line['id'], "filename": str(image_names[line['id']]), "url": line['url'], "location": {"lon": lon, "lat": lat}}
            except:
                print("Threw an exception on: " + line['id'])

    csvfile.close()
    # Write our payloads out to file

    with open('train_attribution_geo.json', 'w') as out_file:
        json.dump(payloads_non_list, out_file, sort_keys=True, indent=4,
                  ensure_ascii=False)

# now create our vector
vectors_non_list = make_embeddings_upload.get_features()

# with open('../train_attribution_vectors.json', 'w') as out_file:
#     json.dump(vectors_non_list, out_file, sort_keys=True, indent=4,
#               ensure_ascii=False)


ids, vectors, payloads = [], [], []
# Put them together - need to do this because of the sorting problem - need to get them to line up
id_payload_vectors = []

# We need both the arrays and the JSON item. The JSON item is to accumulate JSON entries for the output file.
json_item = {}

for key, payload in payloads_non_list.items():
    json_item = {}
    payloads.append(payload)
    json_item["payload"] = payload
    vectors.append(vectors_non_list[key])
    json_item["vector"] = list(vectors_non_list[key].astype(float))
    id_string = str(uuid.uuid3(uuid.NAMESPACE_DNS, payload["url"]))
    ids.append(id_string)
    json_item["id"] = id_string
    id_payload_vectors.append(json_item)

# write ids, payloads, and vectors out to a JSON file
with open("id_payload_vector.json", 'w') as full_file:
    json.dump(id_payload_vectors, full_file, sort_keys=True, indent=4,
              ensure_ascii=False)

# now insert into the collection
uploader = db_upload.DBUpload(512, "images")

uploader.upsert_vectors(ids, vectors, payloads)

print("finished")




