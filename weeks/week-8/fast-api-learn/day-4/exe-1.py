from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


@app.get('/numbers/{n}')
def get_num(n: int):
    if 0 > n:
        raise HTTPException(status_code=400, detail=f'{n} -> negative number')
    return n
