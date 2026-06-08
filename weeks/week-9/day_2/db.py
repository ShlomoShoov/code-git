"""
this file manage the CRUD commands to with the data base

"""
import mysql.connector
from pydantic import BaseModel



HOST = '127.0.0.1'
PASSWORD = 'secret'
DB = 'soldiers_db'
USER = 'root'
PORT = 3306

def get_connection()->mysql.connector:
    """
    create a connection to the database
    """
    return mysql.connector.connect(host=HOST, 
                                   password = PASSWORD,
                                   database = DB,
                                   user = USER,
                                   port = PORT)

def get_all()->list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    query = f"""
            SELECT * FORM {DB}
            """
    cursor.execute(query)
    soldiers = cursor.fetchall()
    
    conn.close()
    cursor.close()
    return soldiers

def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary= True)
    query = f"""
            SELECT FROM {DB} WHERE id == %s
            """
    cursor.execute(query, (soldier_id,))
    soldier = cursor.fetchall()
    conn.close()
    cursor.close()
    return soldier

def create(name, rank, unit) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
            INSERT INTO {DB} (name, rank_, unit) VALUES (%s, %s, %s)
            """
    cursor.execute(query, (name,rank,unit))
    new_id = cursor.lastrowid()

    conn.close()
    cursor.close()
    return new_id

def update(soldier_id, data: dict) -> bool:
    """
    DATA = {"rank":"high","id":5}
    
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
            UPDATE {DB} SET rank_=%s WHERE id=%s

            """
    cursor.execute(query, (data['rank'], soldier_id))
    has_update = cursor.rowcount > 0

    conn.close()
    cursor.close()

    return has_update

def delete(soldier_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
            DELETE FROM  {DB} WHERE id=%s
            """
    cursor.execute(query, (soldier_id,))
    has_deleted = cursor.rowcount > 0

    conn.close()
    cursor.close()

    return has_deleted

