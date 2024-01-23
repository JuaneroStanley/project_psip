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

engine = None

drivername, username, password, database, host, port = None, None, None, None, None, None


def get_db_params():
    drivername = 'postgresql'
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    return drivername, username, password, database, host, port

def create_engine():
    db_params = sqlalchemy.engine.URL.create(
        drivername=drivername,
        username=username,
        password=password,
        database=database,
        host=host,
        port=port)
    print(drivername, username, password, database, host, port)
    return sqlalchemy.create_engine(db_params)

def check_if_schema_exists():
    with engine.connect() as connection:
        connection.execute(CreateSchema("staskrz", if_not_exists=True))
        connection.commit()
    check_if_tables_exist()
    
def check_connection():
    try:
        connection = engine.connect()
        return True
    except Exception as e:
        print(e)
        return False
    
def check_if_tables_exist():
    metadana = sqlalchemy.MetaData(schema="staskrz")
    metadana.reflect(bind=engine)
    keys =  metadana.tables.keys()
    keys = list(str(key) for key in keys)
    if f'staskrz.{User.__tablename__}' not in keys or \
        f'staskrz.{Restaurant.__tablename__}' not in keys or \
        f'staskrz.{Client.__tablename__}' not in keys or \
        f'staskrz.{Courier.__tablename__}' not in keys or \
        f'staskrz.{Order.__tablename__}' not in keys:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    if not check_if_admin_exists():
        add_user_db(create_session(), User(nickname="admin", email="", password="admin"))
     
     
def check_if_admin_exists():
    with create_session() as session:
        user = session.query(User).filter(User.nickname == "admin",User.password=="admin").first()
        if user:
            return True
        else:
            return False     
   
def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_database_if_not_exists():
    if not database_exists(engine.url):
        create_database(engine.url)
        check_if_schema_exists()
    else:
        check_if_schema_exists()
        
def add_user_db(session, user):
    session.add(user)
    session.commit()
    
def add_restaurant_db(session, restaurant):
    session.add(restaurant)
    session.commit()
    
def add_client_db(session, client):
    session.add(client)
    session.commit()
    
def add_courier_db(session, courier):
    session.add(courier)
    session.commit()
    
def add_order_db(session, order):
    session.add(order)
    session.commit()
    
def get_user_role(session, nickname, password):
    user = session.query(User).filter(User.nickname == nickname, User.password == password).first()
    if user:
        return user.role
    else:
        return None
    
