import mysql.connector


HOST = '127.0.0.1'
PASSWORD = 'secret'
DB = 'soldiers_db'
USER = 'root'
PORT = 3306

TABLE = 'soldiers'


def get_connection() -> mysql.connector:
    """
    create a connection to the database
    """
    return mysql.connector.connect(host=HOST,
                                   password=PASSWORD,
                                   database=DB,
                                   user=USER,
                                   port=PORT)


def filter_by_rank(rank: str) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
            SELECT * FROM {TABLE} WHERE rank_ =%s
            """
    cursor.execute(query, (rank,))
    soldiers = cursor.fetchall()
    conn.close()
    cursor.close()

    return soldiers


def filter_by_unit(unit:str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
            SELECT * FROM {TABLE} WHERE unit =%s
            """
    cursor.execute(query, (unit,))
    soldiers = cursor.fetchall()
    conn.close()
    cursor.close()

    return soldiers

def sort_soldiers(sort_type):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = f"""
            SELECT * FROM {TABLE} ORDER BY {sort_type}
            """
    cursor.execute(query)
    soldiers = cursor.fetchall()
    conn.close()
    cursor.close()

    return soldiers


def get_units():
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
            SELECT DISTINCT unit FROM {TABLE}
            """
    cursor.execute(query)
    units = cursor.fetchall()
    conn.close()
    cursor.close()

    return units


def search_by_key_and_value(key: str , value: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
            SELECT * FROM {TABLE} WHERE {key} LIKE %s
            """
    cursor.execute(query, ('%' + value +  '%',))
    units = cursor.fetchall()
    conn.close()
    cursor.close()

    return units