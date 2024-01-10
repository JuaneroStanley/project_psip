from orm.base import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from geoalchemy2 import Geometry

class User(Base):
    __tablename__ = 'user'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nickname = mapped_column(String(64), nullable=False)
    email = mapped_column(String(64), nullable=False)
    password = mapped_column(String(64), nullable=False)
    role = mapped_column(Integer, nullable=False, default=0)
    
    def __repr__(self):
        return '<User %r>' % self.nickname

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(64), nullable=False)
    phone = mapped_column(String(64), nullable=False)
    description = mapped_column(String(64), nullable=False)
    menu = mapped_column(String(64), nullable=False)
    rating = mapped_column(Integer, nullable=False, default=0)
    location = mapped_column(Geometry('POINT'), nullable=False)  
    
    def __repr__(self):
        return '<Restaurant %r>' % self.name
    
class Client(Base):
    __tablename__ = 'client'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(64), nullable=False)
    phone = mapped_column(String(64), nullable=False)
    email = mapped_column(String(64), nullable=False)
    location = mapped_column(Geometry('POINT'), nullable=False)  
    
    def __repr__(self):
        return '<Client %r>' % self.name

class Courier(Base):
    __tablename__ = 'courier'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(64), nullable=False)
    phone = mapped_column(String(64), nullable=False)
    location = mapped_column(Geometry('POINT'), nullable=False)
    status = mapped_column(Integer, nullable=False, default=0)
    
    def __repr__(self):
        return '<Courier %r>' % self.name
    
    
class Order(Base):
    __tablename__ = 'order'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = mapped_column(Integer, ForeignKey(Restaurant.id))
    client_id = mapped_column(Integer, ForeignKey(Client.id))
    courier_id = mapped_column(Integer, ForeignKey(Courier.id))
    status = mapped_column(Integer, nullable=False, default=0)
    location = mapped_column(Geometry('POINT'), nullable=False)
    
    client = relationship('Client', backref='orders')
    courier = relationship('Courier', backref='orders')
    restaurant = relationship('Restaurant', backref='orders')
    
    
    
    def __repr__(self):
        return '<Order %r>' % self.id
    
    