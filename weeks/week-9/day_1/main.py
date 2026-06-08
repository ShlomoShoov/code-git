from fastapi import FastAPI 
import uvicorn 

from db_management import get_soldiers, get_schema
import db_management
app = FastAPI()

@app.post('/setup')
def setup_():
    db_management.setup()

@app.get('/schema')
def get_schema_():
    return get_schema()

@app.get('/soldiers')
def get_soldiers_():
    return get_soldiers()

if __name__ == "__main__":
    uvicorn.run(app)