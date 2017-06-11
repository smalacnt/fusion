"""module models"""

from sqlalchemy import Table
from fusion.mysql.database import metadata

ifcdta = Table('ifc_dta_t', metadata, autoload=True)