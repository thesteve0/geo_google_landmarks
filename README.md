# Instuctions and other stuff

The gist of the demo is:
You are query a subset of the google_landmark images by using the image in the query_image directory.

It is a subset of all the data because:
1. The full dataset of images for download is huge and are not needed for the demo
2. We only saved the encoding for images where we could figure out its coordinates

Encoding all the images would take too much time for a workshop. Instead I have done it already, put it in PostgreSQL, and then dumped the database.

Therefore, the only code that is needed are the ones that are named  *_query.py

You can drive the demo from the main_query.py, the other _query files were created to keep a bit cleaner code.

If you want to look at house I embeded and then uploaded the images I had on my machine, that is all based on main.py. 
Again it relies on the 2 files *_upload.py to keep the code cleaner

## Instructions to prep for running the code
1. `gunzip geo_image_dump_sql`
2. `PGPASSWORD=letmein creatdb -h localhost -U postgres geoimage`
3. `PGPASSWORD=letmein gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage`



## These are notes on building the container

`$ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

https://github.com/mlfoundations/open_clip


`podman run -d -p 5432:5432 -e POSTGRES_PASSWORD=test --name maybe ghcr.io/thesteve0/pg16-full`

```shell

wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1.1/geo_image_dump_sql.gz
wget -qb https://github.com/thesteve0/geo_google_landmarks/releases/download/v0.1/image_query_files.tar.gz

tar -xvf image_query_files.tar.gz

PGPASSWORD=letmein creatdb -h localhost -U postgres geoimage
PGPASSWORD=letmein gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage

```
