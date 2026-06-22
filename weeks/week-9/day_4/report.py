from day_2.db import get_connection, TABLE

def get_summary():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            summary = {}
            query_for_count = f"""
                        SELECT COUNT(*) as total FROM {TABLE}
                    """
            cursor.execute(query_for_count)
            total = cursor.fetchone()['total']
            summary['total'] = total
            query_for_active = f"""
                    SELECT COUNT(*) as active FROM {TABLE} WHERE active = True

                    """
            
            cursor.execute(query_for_active)
            active = cursor.fetchone()['active']
            summary['active'] = active
            summary['inactive'] = total-active
    return summary


def count_by_unit():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            query = f"""
                    SELECT unit, COUNT(unit) as total FROM {TABLE} GROUP BY unit ORDER BY  unit DESC

                    """
            cursor.execute(query)
            units = cursor.fetchall()
    return units


def get_units_with_multiple_soldiers():
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            query = f"""
                    SELECT unit FROM {TABLE} GROUP BY unit HAVING COUNT(unit) > 1
                    """
            cursor.execute(query)
            units = cursor.fetchall()
    return units



    