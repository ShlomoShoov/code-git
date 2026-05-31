from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get('/ping')
def pong():
    return {'status':'pong'}

@app.get('/ping/{name}')
def greet(name:str):
    return {'msg':f'hello {name}'}


if __name__ == '__main__':
    uvicorn.run(app)