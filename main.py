from fastapi.responses import Response, JSONResponse, HTMLResponse, FileResponse
from fastapi import FastAPI, File, UploadFile, Depends
from pydantic import BaseModel
from typing import Optional
import sys, os, io


from nefnir import Nefnir

__version__ = 0.1

app = FastAPI()
nefnir = Nefnir()


def error(errors):
    return JSONResponse(content=({"failure":{"errors":[errors]}}))


@app.get('/', response_class=HTMLResponse)
def home() -> str:
    return """
<html>
    <head><title>Nefnir API</title></head>
    <body>
        <h1>Nefnir API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(__version__)


class LemmaInput(BaseModel):
    type: Optional[str] = "text"
    content: str

@app.post('/lemmatizer')
def lemmatizerAPI(request : LemmaInput): 
    global nefnir
    tokens = request.content.split(' ')
    if len(tokens) % 2 != 0:
        return error({"code":"lemmatiser", "text":"bad input", "detail":{'traceback':traceback.format_exc()}})
    texts = []
    try:
        for i in range(0,len(tokens),2):
            form, tag = tokens[i], tokens[i+1]
            if form:
                lemma = nefnir.lemmatize(form, tag)
                texts.append({'content':form, 'features':{'tag':tag, 'lemma': lemma}})
    except ValueError:
        return error({"code":"lemmatiser", "text":"unable to lemmatize", "detail":{'traceback':traceback.format_exc()}})
    return JSONResponse(content={"response":{"type":"texts","texts":texts}})
