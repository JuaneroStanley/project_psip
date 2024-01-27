from orm.base import Base
from orm.ddl import User, Restaurant, Client, Courier, Order
from sqlalchemy_utils import database_exists, create_database
import sqlalchemy
from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker
import dotenv
import os

env = dotenv.load_dotenv('./.env')
# db_params = sqlalchemy.engine.URL.create(
#     drivername='postgresql',
#     username=os.getenv("POSTGRES_USER"),
#     password=os.getenv("POSTGRES_PASSWORD"),
#     database=os.getenv("POSTGRES_DB"),
#     host=os.getenv("POSTGRES_HOST"),
#     port=os.getenv("POSTGRES_PORT"))

engine = None

drivername, username, password, database, host, port = None, None, None, None, None, None


def get_db_params()->tuple:
    """
    Retrieves the database connection parameters from environment variables.

    Returns:
        tuple[str, str, str, str, str, str]: A tuple containing the drivername, username, password, database, host, and port.
    """
    drivername = 'postgresql'
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    return drivername, username, password, database, host, port

def create_engine() -> sqlalchemy.engine.base.Engine:
    """
    Creates and returns a SQLAlchemy engine based on the provided database parameters.

    Returns:
        sqlalchemy.engine.base.Engine: The SQLAlchemy engine object.
    """
    db_params = sqlalchemy.engine.URL.create(
        drivername='postgresql',
        username=username,
        password=password,
        database=database,
        host=host,
        port=port)
    print(drivername, username, password, database, host, port)
    return sqlalchemy.create_engine(db_params)

def check_if_schema_exists()->None:
    """
    Checks if the 'staskrz' schema exists in the database. If not, creates it.
    """
    with engine.connect() as connection:
        connection.execute(CreateSchema("staskrz", if_not_exists=True))
        connection.commit()
    check_if_tables_exist()
    
def check_connection() -> bool:
    """
    Check the connection to the database.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        connection = engine.connect()
        return True
    except Exception as e:
        print(e)
        return False
    
def check_if_tables_exist()->None:
    """
    Checks if the required tables exist in the database. If any of the tables are missing,
    it drops all existing tables and creates them again. Additionally, if the admin user
    does not exist, it adds the admin user to the database.
    """
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
     
     
def check_if_admin_exists()->bool:
    """
    Check if an admin user exists in the database.

    Returns:
        bool: True if an admin user exists, False otherwise.
    """
    with create_session() as session:
        user = session.query(User).filter(User.nickname == "admin", User.password == "admin").first()
        if user:
            return True
        else:
            return False
   
def create_session() -> sqlalchemy.orm.session.Session:
    """
    Creates a new session using the configured engine.

    Returns:
        sqlalchemy.orm.session.Session: The created session.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_database_if_not_exists()->None:
    """
    Creates a database if it does not already exist.
    """
    if not database_exists(engine.url):
        create_database(engine.url)
        check_if_schema_exists()
    else:
        check_if_schema_exists()
        
def add_user_db(session, user:User)->None:
    session.add(user)
    session.commit()
    
def add_restaurant_db(session, restaurant:Restaurant)->None:
    session.add(restaurant)
    session.commit()
    
def add_client_db(session, client:Client)->None:
    session.add(client)
    session.commit()
    
def add_courier_db(session, courier:Courier)->None:
    session.add(courier)
    session.commit()
    
def add_order_db(session, order:Order)->None:
    session.add(order)
    session.commit()
    
