from fastapi import FastAPI, HTTPException
from typing import Literal
import uvicorn
import queries
app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app)