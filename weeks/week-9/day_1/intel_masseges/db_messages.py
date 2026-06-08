from db_setting import connect_to_db

def get_all_massages()->list:
    """
    return the data-base full table     
    """
    conn = connect_to_db()
    
