import mysql.connector

HOST = '127.1.1.0'
USER = 'root'
DB = 'soldiers_db'
PASSWORD = 'secret'
PORT = 3306


def get_connection()->mysql.connector.connect:
    return mysql.connector.connect(
        host = HOST,
        user = USER,
        database = DB,
        password = PASSWORD,
        port = PORT
    )


def get_all():
    pass