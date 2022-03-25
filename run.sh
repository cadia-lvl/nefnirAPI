docker stop nefnir
docker container rm nefnir
docker build . -t glaciersg/nefnir_api:v1.0.0
docker run -d -p 8080:8080 --name=nefnir glaciersg/nefnir_api:v1.0.0
