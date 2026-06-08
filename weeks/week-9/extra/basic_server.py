from fastapi import FastAPI
import uvicorn 
import mysql.connector

app = FastAPI()

conn = mysql.connector.connect(
    host="127.0.0.1", port=3306,
    user="root",
      password="secret",
    database="soldiers_db"
    )

cursor = conn.cursor()

@app.get('/soldiers_sql')
def get_soldiers():
    cursor.execute("DESCRIBE soldiers")
    return cursor.fetchall()



if __name__ == '__main__':
    uvicorn.run(app)
    conn.close()
    cursor.close()