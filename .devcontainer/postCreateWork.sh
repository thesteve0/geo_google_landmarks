#! /bin/bash

wget dbbackup
wget testimages

tar -xvf image_query_files.tar.gz

sudo su
su postgres

PGPASSWORD=letmein creatdb -h localhost -U postgres geoimage
PGPASSWORD=letmein gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage

