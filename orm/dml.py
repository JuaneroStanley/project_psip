from orm.base import Base
from orm.ddl import User, Restaurant, Client, Courier, Order
from sqlalchemy_utils import database_exists, create_database
import sqlalchemy
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker
import dotenv
import os

env = dotenv.load_dotenv('./.env')
db_params = sqlalchemy.engine.URL.create(
    drivername='postgresql',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    database=os.getenv("POSTGRES_DB"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"))

engine = sqlalchemy.create_engine(db_params)

def check_if_schema_exists():
    with engine.connect() as connection:
        connection.execute(CreateSchema("staskrz", if_not_exists=True))
        connection.commit()
    check_if_tables_exist()
    
    
def check_if_tables_exist():
    inspector = sqlalchemy.inspect(engine)
    if User.__tablename__ not in inspector.get_table_names() or \
        Restaurant.__tablename__ not in inspector.get_table_names() or \
        Client.__tablename__ not in inspector.get_table_names() or \
        Courier.__tablename__ not in inspector.get_table_names() or \
        Order.__tablename__ not in inspector.get_table_names():
        
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)