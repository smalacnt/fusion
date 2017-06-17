"""module util: api util"""

from fusion.mysql.database import engine

def get_dbtime():
    """return database time"""
    (time, ) = engine.execute('SELECT current_timestamp').first()
    return time