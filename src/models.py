import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    favorites = relationship("Favorite")

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    mass = Column(Integer)
    internal_differentiation = Column(String(100))
    atmosphere = Column(String(100))
    population = Column(Integer)
    moons = Column(Integer)
    rotation_time = Column(Integer)
    favorites = relationship("Favorites")

class Characters(Base): 
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    birth_date = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    eye_color = Column(String(100))
    hair_color = Column(String(100))
    skin_tone = Column(String(100))
    gender = Column(String(100))
    favorites = relationship("Favorites")

class Favorite(Base):
    __tablename__ = 'Favorite'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters = relationship("Characters")
    planets = relationship("Planets")
    user = relationship("User", back_populates="users")
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
