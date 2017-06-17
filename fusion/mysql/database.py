"""mysql database engine """
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine(
    'mysql://fusion:fusion@127.0.0.1:3306/fusion', convert_unicode=True, echo=True,
    pool_size=8, max_overflow=4, pool_timeout=30)
metadata = MetaData(bind=engine)
