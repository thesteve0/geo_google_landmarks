#! /bin/bash

wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1.1/geo_image_dump_sql.gz
wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1/image_query_files.tar.gz

tar -xvf image_query_files.tar.gz

sudo su
su postgres

PGPASSWORD=letmein creatdb -h localhost -U postgres geoimage
PGPASSWORD=letmein gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage

