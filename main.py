from fastapi import FastAPI
from fastapi.params import Body
from db import get_all_posts,creat_new_post
from schema.serializer import PostCreateSerailizer


app = FastAPI()

@app.get("/")
def hello():
    return get_all_posts()


@app.post("/")
def hia(payload:PostCreateSerailizer):
    return creat_new_post(payload.dict())
    
    

print(__name__)
