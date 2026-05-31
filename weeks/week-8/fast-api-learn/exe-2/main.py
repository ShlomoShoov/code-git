from fastapi import FastAPI
import uvicorn
from datetime import datetime
app = FastAPI()

@app.get('/')
def home():
    return  {"service": "my-api", "version": "1.0"}

@app.get('/status')
def get_status():
    return {'server_name':'my_server','time':datetime.now().time()}

@app.get('/users/admin')
def get_admin():
    return {"role": "admin", "access": "full"}

@app.get('/users/{user_id}')
def get_user(user_id):
    return {'user_id':user_id, 'mail':'exemple@gmail.com', 'name':'unknown'}

@app.get('/calc/{a}/{op}/{b}')
def calc(a:int,b:int,op:str)->dict:
    result_dict = {"operation": op}
    calc_dict = {'add':lambda x,y: x+y,
                 'sub': lambda x,y: x-y,
                 'mul': lambda x,y: x*y,
                 'div': lambda x,y: x/y}
    if op in calc_dict:
        try:
            result_dict['result'] = calc_dict[op](a,b)
            
        except ZeroDivisionError as e:
            result_dict['result'] = e.args[0]
    else:
        result_dict['result'] = 'unsupported operator '
    
    return result_dict

if __name__ == '__main__':
    uvicorn.run(app)

