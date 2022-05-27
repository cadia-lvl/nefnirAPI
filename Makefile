build:
	docker build . -t nefnir_api
run:
	docker run -d -p 8080:8080 --name=nefnir nefnir_api
stop:
	docker stop nefnir
	docker rm nefnir
