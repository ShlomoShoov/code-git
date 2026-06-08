from fastapi import FastAPI, HTTPException
import uvicorn 
from pydantic import BaseModel

from db import get_all, get_by_id, create, delete, update

class NewSoldier(BaseModel):
    name : str
    rank : str
    unit : str

class UpdateSoldier(BaseModel):
    rank : str


app = FastAPI()

@app.get("/soldiers")
def get_soldiers():
    return get_all()

@app.get("/soldiers/{id}")
def get_soldier(id:int):
    soldier = get_by_id(id)
    if not soldier:
        raise HTTPException(status_code=404,detail="not found")
    return soldier

@app.post("/soldiers",status_code=201)
def add_soldier(data:NewSoldier):
    return create(**data.model_dump())


@app.put("/soldiers/{id}")
def update_soldier(id:int, data:UpdateSoldier):
    has_update = update(id, data.model_dump())
    if not has_update:
        raise HTTPException(status_code=404,detail="not found")
    
@app.delete("/soldiers/{id}")
def delete_soldier(id):
    deleted = delete(id)
    if not deleted:
        raise HTTPException(status_code=404,detail="not found")

