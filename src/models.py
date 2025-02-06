import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    las_name = Column(String(250), nullable=False)
    email = Column(String(150), nullable= False)
    password = Column(String(250), nullable=False)
    data_suscription = Column(String(250), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_character = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorite_id = Column(Integer, ForeignKey('favorites_characters.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorite_id = Column(Integer, ForeignKey('favorites_planets.id'))
    user = relationship(User)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_vehicle = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorite_id = Column(Integer, ForeignKey('favorites_vehicles.id'))
    user = relationship(User)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table favorites.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    total_likes = Column(String(500))
    user = relationship(User)

class favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    likes_planets = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)

class favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)    
    likes_characteres = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))    
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)

class favorites_vehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id = Column(Integer, primary_key=True)    
    likes_vehicles = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))    
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
