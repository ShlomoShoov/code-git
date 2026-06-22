import mysql.connector

import time

PORT = 3306
PASSWORD = 'secret'
USER = 'root'
HOST = "localhost"
DB = 'soldiers_db'



def get_connector():
    conn = mysql.connector.connect(
                        host='127.0.0.1',
                       user = USER,
                       password = PASSWORD,
                       port= PORT,
                       database= DB)
    return conn
    

def setup():
    conn = get_connector()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS soldiers 
    (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            rank_ VARCHAR(50),
            unit VARCHAR(100),
            active BOOLEAN DEFAULT TRUE
            )
            
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

def get_schema():
    conn = get_connector()
    cursor = conn.cursor()

    query = """
            DESCRIBE soldiers
            """
    cursor.execute(query)
    rows = cursor.fetchall()


    conn.close()
    cursor.close()

    return rows


def get_soldiers():
    conn = get_connector()
    cursor = conn.cursor()

    query = f"""
            SELECT * FROM {DB}

            """
    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()
    cursor.close()

    return rows

