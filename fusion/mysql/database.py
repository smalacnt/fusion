"""mysql database engine """
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql://fusion:fusion@127.0.0.1:3306/fusion', convert_unicode=True, echo=True)
metadata = MetaData(bind=engine)
conn = engine.connect()