from fastapi import FastAPI, HTTPException
import uvicorn 

from pydantic import BaseModel


from day_1.db_management import get_schema
import day_1.db_management as db_management


from day_2.db import get_all, get_by_id, create, delete, update

import day_3.queries as queries

import  day_4.report  as report

class NewSoldier(BaseModel):
    name : str
    rank : str 
    unit : str

class UpdateSoldier(BaseModel):
    rank : str


app = FastAPI()




@app.post('/setup')
def setup_():
    db_management.setup()

@app.get('/schema')
def get_schema_():
    return get_schema()




@app.get("/soldiers")
def get_soldiers(rank:str|None = None, sort:Literal['DESC', 'ASC'] | None = None, unit:str = None):
    if rank is not None:
        return queries.filter_by_rank(rank)
    elif sort is not None:
        return  queries.sort_soldiers(sort)
    elif unit is not None:
        return queries.filter_by_unit(unit)
    else:
        return []
    
@app.get("/soldiers/units")
def get_unique_units():
    return queries.get_units()

@app.get('/soldiers/search')
def search(name:str|None=None):
    if name is not None:
        return queries.search_by_key_and_value(key='name', value=name)


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
    





@app.get('/stats/summary')
def get_summary():
    return report.get_summary()


@app.get("/stats/understaffed")
def get_understaffed():
    return report.get_units_with_multiple_soldiers()

@app.get("/stats/units")
def get_units():
    return report.count_by_unit()
