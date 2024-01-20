import sqlalchemy.orm
from sqlalchemy import MetaData

metadata_obj = MetaData(schema="staskrz")


Base = sqlalchemy.orm.declarative_base(metadata=metadata_obj)