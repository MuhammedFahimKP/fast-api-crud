from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index() -> dict:
    return  {
        "user":{
            "name":"hai"
        }
    }
    
@app.get('/about/')    
def about() -> dict:
    return {
        'data':'about page'
    }    