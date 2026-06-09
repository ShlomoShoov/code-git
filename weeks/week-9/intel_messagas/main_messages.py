from fastapi import FastAPI, HTTPException
import uvicorn 
from setup import setup_table
from messages_db import get_schema, get_all, get_by_id

app = FastAPI()

@app.get('/schema')
def show_schema():
    return get_schema()

@app.get('/messages')
def show_all_messages():
    return get_all()

@app.get('/massages/{id}')
def get_msg_by_id(id:int):
    msg = get_by_id(id)
    if msg is None:
        raise HTTPException(status_code=404, detail='not_found')
    return msg

if __name__ == "__main__":
    setup_table()
    uvicorn.run(app)