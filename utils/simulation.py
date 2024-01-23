import utils.backend as bknd
import orm.dml as dml
from orm.base import Base
from faker import Faker


def simulate():
    print("Simulating...")
    engine = dml.engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fake = Faker()
    for i in range(10):
        bknd.add_restaurant(name=fake.name(), phone=fake.phone_number(), description=fake.email(),rating=2.3,location= f'POINT({fake.longitude()} {fake.latitude()})')
        bknd.add_client(fake.name(), fake.phone_number(), fake.email(), f'POINT({fake.longitude()} {fake.latitude()})')
        bknd.add_courier(fake.name(), fake.phone_number(), f'POINT({fake.longitude()} {fake.latitude()})', 0)
        client = bknd.get_client(i+1)
        courier = bknd.get_courier(i+1)
        restaurant = bknd.get_restaurant(i+1)
        bknd.add_order(restaurant.id, client.id, courier.id, 0, fake.email())