from fastapi import FastAPI
import uvicorn

"""
file to handle the to-do server
"""

BASE_URL = '127.0.0.1'
app = FastAPI()

# end point of the basic home page
@app.get('/')
def home_page():
    return {'msg':'welcome to the to do list system :)', 'links':f'{BASE_URL}/users/'}



if __name__ == '__main__':
    pass
    # uvicorn.run()