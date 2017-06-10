"""module util """
from fusion.mysql.conn import DB

def get_dbtime():
    """get database current time """
    cur = DB.cursor()
    cur.execute('SELECT current_timestamp')
    (time,) = cur.fetchone()
    return time
