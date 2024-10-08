#! /bin/bash

wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1.1/geo_image_dump_sql.gz
wait
wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1/image_query_files.tar.gz
wait

echo done downloading

tar -xvf image_query_files.tar.gz
wait
echo untarred

PGPASSWORD=letmein /usr/bin/createdb -h localhost -U postgres geoimage
wait
PGPASSWORD=letmein /usr/bin/gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage
wait

pip install openai-clip

