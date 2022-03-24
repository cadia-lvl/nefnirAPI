FROM pypy:3

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app
RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

WORKDIR /usr/src/app
RUN git clone https://github.com/GlacierSG/nefnir.git

WORKDIR /usr/src/app/nefnir
COPY . .

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0

