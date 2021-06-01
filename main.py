import hashlib
from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import Response, JSONResponse, HTMLResponse, FileResponse
import tempfile
import sys, os, io
sys.path.append("nefnir")
from nefnir import *

__version__ = 0.1

app = FastAPI()

#lemmatizer("tagged.txt", "lemmatizer.txt")

ALLOWED_FILE_EXTENSIONS = [".txt"]

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

        
def lemmatizerAPI_(file:UploadFile = File(...)):
    global ALLOWED_FILE_EXTENSIONS
    if file.filename != '':
        file_ext = os.path.splitext(file.filename)[1]
        if file_ext not in ALLOWED_FILE_EXTENSIONS:
            abort(400)
        file_content = file.file.read()
        upload_fd, upload_path = tempfile.mkstemp(suffix='.txt')
        lemm_fd, lemm_path = tempfile.mkstemp(suffix='.txt') 
        with os.fdopen(upload_fd, 'wb') as f:
            f.write(file_content)
        lemmatizer(upload_path, lemm_path)
        try:
            yield lemm_path
        finally:
            # cleanup temp files
            os.unlink(lemm_path)
            os.unlink(upload_path)
    else:    
        abort(400)
@app.post('/lemmatizer')
async def lemmatizerAPI(file_path=Depends(lemmatizerAPI_)): 
        return FileResponse(file_path)
