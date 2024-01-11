import orm.dml as dml
from orm.dml import User, Restaurant, Client, Courier, Order,create_session

def add_user(nickname, email, password, role):
    user = User(nickname=nickname, email=email, password=password, role=role)
    with create_session() as session:
        dml.add_user_db(session, user)
    
def add_restaurant(name, phone, description, menu, rating, location):
    restaurant = Restaurant(name=name, phone=phone, description=description, menu=menu, rating=rating, location=location)
    with create_session() as session:
        dml.add_restaurant_db(session, restaurant)
        
def add_client(name, phone, email, location):
    client = Client(name=name, phone=phone, email=email, location=location)
    with create_session() as session:
        dml.add_client_db(session, client)
        
def add_courier(name, phone, location, status):
    courier = Courier(name=name, phone=phone, location=location, status=status)
    with create_session() as session:
        dml.add_courier_db(session, courier)
        
def add_order(restaurant_id, client_id, courier_id, status, location, description):
    order = Order(restaurant_id=restaurant_id, client_id=client_id, courier_id=courier_id, status=status, location=location, description=description)
    with create_session() as session:
        dml.add_order_db(session, order)

def get_all_restaurants():
    with create_session() as session:
        restaurants = session.query(Restaurant).all()
        return restaurants
    
def get_all_clients():
    with create_session() as session:
        clients = session.query(Client).all()
        return clients
    
def get_all_couriers():
    with create_session() as session:
        couriers = session.query(Courier).all()
        return couriers

def get_all_orders():
    with create_session() as session:
        orders = session.query(Order).all()
        return orders

def get_all_orders_by_client(client_id):
    with create_session() as session:
        orders = session.query(Order).filter(Order.client_id == client_id).all()
        return orders

def get_all_orders_by_restaurant(restaurant_id):
    with create_session() as session:
        orders = session.query(Order).filter(Order.restaurant_id == restaurant_id).all()
        return orders
    
def get_all_orders_by_courier(courier_id):
    with create_session() as session:
        orders = session.query(Order).filter(Order.courier_id == courier_id).all()
        return orders

def edit_restaurant(id, name, phone, description, menu, rating, location):
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        if restaurant:
            restaurant.name = name
            restaurant.phone = phone
            restaurant.description = description
            restaurant.menu = menu
            restaurant.rating = rating
            restaurant.location = location
            session.commit()
            return True
        else:
            return False
        
def edit_client(id, name, phone, email, location):
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        if client:
            client.name = name
            client.phone = phone
            client.email = email
            client.location = location
            session.commit()
            return True
        else:
            return False
        
def edit_courier(id, name, phone, location, status):
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        if courier:
            courier.name = name
            courier.phone = phone
            courier.location = location
            courier.status = status
            session.commit()
            return True
        else:
            return False
        
def edit_order(id, restaurant_id, client_id, courier_id, status, location, description):
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        if order:
            order.restaurant_id = restaurant_id
            order.client_id = client_id
            order.courier_id = courier_id
            order.status = status
            order.location = location
            order.description = description
            session.commit()
            return True
        else:
            return False
        
def delete_restaurant(id):
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        if restaurant:
            session.delete(restaurant)
            session.commit()
            
def delete_client(id):
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        if client:
            session.delete(client)
            session.commit()
            
def delete_courier(id):
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        if courier:
            session.delete(courier)
            session.commit()
            
def delete_order(id):
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        if order:
            session.delete(order)
            session.commit()