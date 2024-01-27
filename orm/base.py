import sqlalchemy.orm
from sqlalchemy import MetaData


"""
Provides a Base object for all ORM actions.
"""
metadata_obj = MetaData(schema="staskrz")


Base = sqlalchemy.orm.declarative_base(metadata=metadata_obj)