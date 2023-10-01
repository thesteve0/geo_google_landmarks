import requests
from bs4 import BeautifulSoup

from csv import DictReader
from pathlib import Path
import re
import csv

import make_embeddings_play

image_path = Path("../test_images")

metadata_path = "../train_attribution.csv"
image_names = {}

for path in image_path.rglob('*.*'):
    match = re.search('.*(\w{16})\.jpg$', str(path))
    image_names[match.group(1)] = path

csvfile = open(metadata_path, "r", encoding='utf-8')
csvlines = DictReader(csvfile)

payloads = {}
i= 1
for line in csvlines:
    if line['id'] in image_names:
        page = requests.get(line['url'])
        html = BeautifulSoup(page.text, features="html.parser")
        our_tag = html.find('a', {"data-style": "osm-intl"})
        if our_tag is not None:
            lat = our_tag.attrs["data-lat"]
            lon = our_tag.attrs["data-lon"]

            # We have our payload at this point
            print("found one " + line['id'] + " : " + line['url'] + " coords: " + str(lat) + ", " + str(lon))
            payloads[line['id']] = {"picture": line['id'], "filename": match.string, "url": line['url'], "location": {"lon": lon, "lat": lat}}

csvfile.close()
# now create our vector
vectors = make_embeddings_play.get_features()

# now insert into the collection

    # if i <= 10:
    #     print(str(line))
    #     i = i + 1
    # else:
    #     break





