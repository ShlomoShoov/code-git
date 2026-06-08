"""
this file contain the main data for our 
intel massages table management and a function set that table up

"""

import mysql.connector

HOST = '127.0.0.1'
PASSWORD = 'secret'
DB = 'soldiers_db'
USER = 'root'
PORT = 3306

SCHEMA = """
        id INT PRIMARY KEY AUTO_INCREMENT,
        unit VARCHAR(100) NOT NULL, 
        classification ENUM('unclassified','confidential','secret','top_secret'),
        content TEXT NOT NULL,
        source VARCHAR(100),
        created_at DATETIME DEFAULT NOW()
        """

def connect_to_db()->mysql.connector:
    """
    create a connector and return 
    **note** 
    if you create a connector you *must* close it
    use conn.close()
    
    """
    return mysql.connector.connect(host= HOST,
                            password= PASSWORD,
                            database= DB,
                            user= USER,
                            port= PORT)



def setup_table()-> None:
    """
    set up a table, if exists do nothing
    
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"""
                CREATE TABLE IF NOT EXISTS intel_messages,
                ({SCHEMA})
                """
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

