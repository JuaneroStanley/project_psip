import orm.dml as dml
from orm.dml import User, Restaurant, Client, Courier, Order,create_session
import geopy

def add_user(nickname, email, password):
    user = User(nickname=nickname, email=email, password=password)
    with create_session() as session:
        dml.add_user_db(session, user)
    
def add_restaurant(name, phone, description, rating, location):
    restaurant = Restaurant(name=name, phone=phone, description=description, rating=rating, location=location)
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
        
def add_order(restaurant_id, client_id, courier_id, status, description):
    order = Order(restaurant_id=restaurant_id, client_id=client_id, courier_id=courier_id, status=status, description=description)
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

def edit_restaurant(id:int, name:str, phone:str, description:str, rating:str, location:str):
    """
    Edit the details of a restaurant.

    Args:
        id (int): The ID of the restaurant to be edited.
        name (str): The new name of the restaurant.
        phone (str): The new phone number of the restaurant.
        description (str): The new description of the restaurant.
        rating (float): The new rating of the restaurant.
        location (str): The new location in WKT format of the restaurant.

    Returns:
        bool: True if the restaurant was successfully edited, False otherwise.
    """
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        if restaurant:
            restaurant.name = name
            restaurant.phone = phone
            restaurant.description = description
            restaurant.rating = rating
            restaurant.location = location
            session.commit()
            return True
        else:
            return False
        
def edit_client(id:int, name:str, phone:str, email:str, location:str)->bool:
    
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        if client:
            client.name = name
            client.phone = phone
            client.rating = email
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
        
def edit_order(id, restaurant_id, client_id, courier_id, status, description):
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        if order:
            order.restaurant_id = restaurant_id
            order.client_id = client_id
            order.courier_id = courier_id
            order.status = status
            order.description = description
            session.commit()
            return True
        else:
            return False
        
def delete_restaurant(id):
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        orders = session.query(Order).filter(Order.restaurant_id == id).all()
        if restaurant:
            for order in orders:
                session.delete(order)
            session.delete(restaurant)
            session.commit()
            
def delete_client(id):
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        orders = session.query(Order).filter(Order.client_id == id).all()
        if client:
            for order in orders:
                session.delete(order)
            session.delete(client)
            session.commit()
            
def delete_courier(id):
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        orders = session.query(Order).filter(Order.courier_id == id).all()
        if courier:
            for order in orders:
                session.delete(order)
            session.delete(courier)
            session.commit()
            
def delete_order(id):
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        if order:
            session.delete(order)
            session.commit()

def get_order_status(status_int):
    if status_int == 0:
        return 'Delivered'
    elif status_int == 1:
        return 'Picked up'
    elif status_int == 2:
        return 'Preparing'
    
def get_courier_status(status_int):
    if status_int == 0:
        return 'Available'
    elif status_int == 1:
        return 'Delivering'
    elif status_int == 2:
        return 'Unavailable'
    
    
def get_restaurant(id):
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        return restaurant
    
def get_client(id):
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        return client
    
def get_courier(id):
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        return courier
    
def get_order(id):
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        return order

def check_user(nickname, password):
    with create_session() as session:
        user = session.query(User).filter(User.nickname == nickname, User.password == password).first()
        if user:
            return True
        else:
            return False
        
def client_by_name(name):
    with create_session() as session:
        client = session.query(Client).filter(Client.name == name).first()
        return client

def restaurant_by_name(name):
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.name == name).first()
        return restaurant
    
def courier_by_name(name):
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.name == name).first()
        return courier
    
