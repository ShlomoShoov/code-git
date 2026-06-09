import mysql.connector

HOST = '127.1.1.0'
USER = 'root'
DB = 'soldiers_db'
PASSWORD = 'secret'
PORT = 3306

TABLE = 'messages'

def get_connection()->mysql.connector.connect:
    return mysql.connector.connect(
        host = HOST,
        user = USER,
        database = DB,
        password = PASSWORD,
        port = PORT
    )

def get_schema():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = f"""
            DESCRIBE {TABLE} 

            """
    cursor.execute(query)

    rows = cursor.fetchall()


    conn.close()
    cursor.close()
    return rows


def get_all():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = f""" 
            SELECT * FROM {TABLE}
            """
    cursor.execute(query)

    data = cursor.fetchall()

    conn.close()
    cursor.close()

    return data


def get_by_id(msg_id:int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f""" 
            SELECT * FROM {TABLE} WHERE id=%s
            """
    cursor.execute(query,(msg_id,))

    data = cursor.fetchone()

    conn.close()
    cursor.close()

    return data

