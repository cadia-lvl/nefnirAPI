docker stop nefnir
docker container rm nefnir
docker build . -t nefnir:v1
docker run -d -p 8080:8080 --name=nefnir nefnir:v1
