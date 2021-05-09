from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from gendocx import genDocument
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

HOST_NAME = os.getenv("HOST_NAME")

app = FastAPI()

app.mount('/static', StaticFiles(directory="document"), name="static")

class GenDoc(BaseModel):
    title: str
    user: str
    company: str

class DelFile(BaseModel):
    filename: str

@app.post('/')
def generate_document(input: GenDoc):
    url = f'{HOST_NAME}/static/generate_{input.user}_document.docx'

    rs = genDocument(input.title, input.user, input.company)

    ret = {
        "status": rs,
        "download": url
    }

    return ret

@app.delete('/deletefile')
def delete_file(input: DelFile):
    file_name = f'generate_{input.filename}_document.docx'
    file_path = f'./document/{file_name}'
    if os.path.exists(file_path):
        os.remove(file_path)
        return f'delete file {input.filename} success'
    else:
        return 'file does no exist'
