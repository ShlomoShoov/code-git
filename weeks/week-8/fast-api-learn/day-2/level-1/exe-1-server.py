from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get('/greet')
def greet(name:str = 'World')->dict:
    """
    return greeting dict with the name or default name
    
    """
    return {'msg':f'Hello, {name}!'}

if __name__ == '__main__':
    uvicorn.run(app=f'{__name__}:app',reload= True)