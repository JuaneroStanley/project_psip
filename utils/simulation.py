import utils.backend as bknd
import orm.dml as dml
from orm.base import Base
from orm.dml import engine
from faker import Faker


def simulate():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fake = Faker()
    for i in range(10):
        bknd.add_restaurant(name=fake.name(), phone=fake.phone_number(), description=fake.email(),menu="wew",rating=2.3,location= f'POINT({fake.longitude()} {fake.latitude()})')
        bknd.add_client(fake.name(), fake.phone_number(), fake.email(), f'POINT({fake.longitude()} {fake.latitude()})')
        bknd.add_courier(fake.name(), fake.phone_number(), f'POINT({fake.longitude()} {fake.latitude()})', 0)
        with dml.create_session() as session:
            client = dml.get_client(session,i+1)
            courier = dml.get_courier(session,i+1)
            restaurant = dml.get_restaurant(session,i+1)
        bknd.add_order(restaurant.id, client.id, courier.id, 0, fake.email())