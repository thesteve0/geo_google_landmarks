`$ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

https://github.com/mlfoundations/open_clip


`podman run -d -p 5432:5432 -e POSTGRES_PASSWORD=test --name maybe ghcr.io/thesteve0/pg16-full`

```shell
tar -xvf image_query_files.tar.gz

sudo su
su postgres

PGPASSWORD=letmein creatdb -h localhost -U postgres geoimage
PGPASSWORD=letmein gunzip -c geo_image_dump_sql.gz | psql -h localhost -U postgres geoimage

```
