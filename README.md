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
