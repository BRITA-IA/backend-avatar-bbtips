from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get('/')
def root():
    return {'hello': 'Word'}


app.get('/test')
def test():
    return {'data': 'data from backend'}