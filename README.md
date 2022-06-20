# nefnir API
This is an API for [nefnir](https://github.com/jonfd/nefnir) using the [ELG specification](https://european-language-grid.readthedocs.io/en/stable/all/A3_API/LTInternalAPI.html#basic-api-pattern).
The API is wrapped in a [docker container](https://www.docker.com/) and is implemented using [fastapi](https://github.com/tiangolo/fastapi).

# Getting started
```bash
make build
make run
```

# API calls
All the API calls use post and input/outputs are in a json format.
Further details about the api calls are automatically generated when the container is run and can be found in /docs or /redoc

| HTTP METHOD | Description |
| ----------- | --------------- |
| /lemmatizer | Takes in icelandic text and tag for each token in the text and returns the lemma for each token. |


# Testing
test files can be found in `tests/`. There are two tests that can be performed.
1. Normal api tests: this is where you test the api from the running docker image
2. ELG api tests: this is where you run `docker-compose up` and get an instance as if you where running the docker image on ELG. To submit a api call you then need to send a post request to `/process/service`.

# Acknowledgements

[Reykjavik University](https://lvl.ru.is)

This ELG API was developed in EU's CEF project: [Microservices at your service](https://www.lingsoft.fi/en/microservices-at-your-service-bridging-gap-between-nlp-research-and-industry)

# Underlying tool
The underlying lemmatizer is [Nefnir](https://github.com/jonfd/nefnir) by [Jón Daðason](https://github.com/jonfd), which is licensed under this [Apache License 2.0](https://github.com/jonfd/nefnir/blob/master/LICENSE). A forked version of [Nefnir](https://github.com/GlacierSG/nefnir) is cloned when the nefnirAPI docker image is built.
