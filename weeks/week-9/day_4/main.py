import  day_4.report  as report
from fastapi import FastAPI, HTTPException
import uvicorn 


app = FastAPI()


@app.get('/stats/summary')
def get_summary():
    return report.get_summary()


@app.get("/stats/understaffed")
def get_understaffed():
    return report.get_units_with_multiple_soldiers()

@app.get("/stats/units")
def get_units():
    return report.count_by_unit()