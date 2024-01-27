import orm.dml as dml
from orm.dml import User, Restaurant, Client, Courier, Order,create_session
import geopy


is_logged_in = False
def add_user(nickname:str, email:str, password:str):
    """
    Creates a User object calls dml.add_user_db function.
    """
    user = User(nickname=nickname, email=email, password=password)
    with create_session() as session:
        dml.add_user_db(session, user)
    
def add_restaurant(name:str, phone:str, description:str, rating:float, location:str):
    """
    Creates a Restaurant object calls dml.add_restaurant_db function.
    Location is string point in WKB format.
    """
    restaurant = Restaurant(name=name, phone=phone, description=description, rating=rating, location=location)
    with create_session() as session:
        dml.add_restaurant_db(session, restaurant)
        
def add_client(name:str, phone:str, email:str, location:str):
    """
    Creates a Client object calls dml.add_client_db function.
    Location is string point in WKB format.
    """
    client = Client(name=name, phone=phone, email=email, location=location)
    with create_session() as session:
        dml.add_client_db(session, client)
        
def add_courier(name:str, phone:str, location:str, status:int):
    """
    Creates a Crourier object calls dml.add_courier_db function.
    Location is string point in WKB format.
    """
    courier = Courier(name=name, phone=phone, location=location, status=status)
    with create_session() as session:
        dml.add_courier_db(session, courier)
        
def add_order(restaurant_id:int, client_id:int, courier_id:int, status:int, description:str):
    """
    Creates a Order object calls dml.add_order_db function.
    
    Args:
        restaurant_id (int): Existing Restaurant id.
        client_id (int): Existing Client id.
        courier_id (int): Existing Courier id.
        status (int): Order status.
        description (str): Order description.
    """
    order = Order(restaurant_id=restaurant_id, client_id=client_id, courier_id=courier_id, status=status, description=description)
    with create_session() as session:
        dml.add_order_db(session, order)

def get_all_restaurants() -> list[Restaurant]:
    """
    Retrieve a list of all restaurants from the database..
    """
    with create_session() as session:
        restaurants = session.query(Restaurant).all()
        return restaurants
    
def get_all_clients() -> list[Client]:
    """
    Retrieve all clients from the database.
    """
    with create_session() as session:
        clients = session.query(Client).all()
        return clients
    
def get_all_couriers()->list[Courier]:
    """
    Retrieve all couriers from the database.
    """
    with create_session() as session:
        couriers = session.query(Courier).all()
        return couriers

def get_all_orders()->list[Order]:
    """
    Retrieve all orders from the database.
    """
    with create_session() as session:
        orders = session.query(Order).all()
        return orders

def get_all_orders_by_client(client_id:int)->list[Order]:
    """
    Retrieve all orders for a given client.
    """
    with create_session() as session:
        orders = session.query(Order).filter(Order.client_id == client_id).all()
        return orders

def get_all_orders_by_restaurant(restaurant_id:int)->list[Order]:
    """
    Retrieve all orders for a given restaurant.
    """
    with create_session() as session:
        orders = session.query(Order).filter(Order.restaurant_id == restaurant_id).all()
        return orders
    
def get_all_orders_by_courier(courier_id:int) -> list[Order]:
    """
    Retrieve all orders associated with a given courier.
    """
    with create_session() as session:
        orders = session.query(Order).filter(Order.courier_id == courier_id).all()
        return orders

def edit_restaurant(id:int, name:str, phone:str, description:str, rating:float, location:str)->bool:
    """
    Edit the details of a restaurant with the given ID.
    Location is string point in WKB format.


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
    """
    Edit the details of a client with the given ID.
    Location is string point in WKB format.


    Returns:
        bool: True if the client was successfully edited, False otherwise.
    """
    
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
        
def edit_courier(id:int, name:str, phone:str, location:str, status:int)->bool:
    """
    Edit the details of a courier with the given ID.
    Location is string point in WKB format.
    
    Returns:
        bool: True if the courier was found and updated successfully, False otherwise.
    """
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
        
def edit_order(id:int, restaurant_id:int, client_id:int, courier_id:int, status:int, description:str):
    """
    Edit an existing order with the specified parameters.
    
    Returns:
        bool: True if the order was successfully edited, False otherwise.
    """
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
        
def delete_restaurant(id:int) -> None:
    """
    Delete a restaurant and its associated orders from the database.
    """
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        orders = session.query(Order).filter(Order.restaurant_id == id).all()
        if restaurant:
            for order in orders:
                session.delete(order)
            session.delete(restaurant)
            session.commit()
            
def delete_client(id:int) -> None:
    """
    Delete a client and his associated orders from the database.
    """
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        orders = session.query(Order).filter(Order.client_id == id).all()
        if client:
            for order in orders:
                session.delete(order)
            session.delete(client)
            session.commit()
            
def delete_courier(id:int) -> None:
    """
    Delete a courier and its associated orders from the database.
    """
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        orders = session.query(Order).filter(Order.courier_id == id).all()
        if courier:
            for order in orders:
                session.delete(order)
            session.delete(courier)
            session.commit()
            
def delete_order(id:int) -> None:
    """
    Delete a order.
    """
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        if order:
            session.delete(order)
            session.commit()

def get_order_status(status_int:int) -> str:
    """
    Returns the corresponding status string based on the given status integer.

    """
    if status_int == 0:
        return 'Delivered'
    elif status_int == 1:
        return 'Picked up'
    elif status_int == 2:
        return 'Preparing'
    
def get_courier_status(status_int:int)->str:
    """
    Returns the corresponding status string based on the given status integer.
    
    """
    if status_int == 0:
        return 'Available'
    elif status_int == 1:
        return 'Delivering'
    elif status_int == 2:
        return 'Unavailable'
    
    
def get_restaurant(id:int)->Restaurant:
    """
    Retrieve a restaurant by its ID.
    """
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.id == id).first()
        return restaurant
    
def get_client(id:int)->Client:
    """
    Retrieve a client by their ID.
    """
    with create_session() as session:
        client = session.query(Client).filter(Client.id == id).first()
        return client
    
def get_courier(id:int)->Courier:
    """
    Retrieve a courier by their ID.
    """
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.id == id).first()
        return courier
    
def get_order(id:int)->Order:
    """
    Retrieve an order by its ID.
    """
    with create_session() as session:
        order = session.query(Order).filter(Order.id == id).first()
        return order

def check_user(nickname:str, password:str)->bool:
    """
    Check if the user exists in the database.
    """
    with create_session() as session:
        user = session.query(User).filter(User.nickname == nickname, User.password == password).first()
        if user:
            return True
        else:
            return False
        
def client_by_name(name:str)->Client:
    """
    Retrieve a client by their name.
    """
    with create_session() as session:
        client = session.query(Client).filter(Client.name == name).first()
        return client

def restaurant_by_name(name:str)->Restaurant:
    """
    Retrieve a restaurant by its name.
    """
    with create_session() as session:
        restaurant = session.query(Restaurant).filter(Restaurant.name == name).first()
        return restaurant
    
def courier_by_name(name:str)->Courier:
    """
    Retrieve a courier by their name.
    """
    with create_session() as session:
        courier = session.query(Courier).filter(Courier.name == name).first()
        return courier
    
