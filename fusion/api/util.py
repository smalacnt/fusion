"""module util: api util"""

from fusion.mysql.database import conn, engine

def get_dbtime():
    """return database time"""
    (time, ) = conn.execute('SELECT current_timestamp').first()
    return time