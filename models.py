from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, Enum, Float, LargeBinary
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True, nullable=False)
    phone = Column(Text)
    fam = Column(Text)
    name = Column(Text)
    otc = Column(Text)
    perevals = relationship("Pereval", back_populates="user")

class Coords(Base):
    __tablename__ = 'coords'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)

class Level(Base):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True)
    winter = Column(Text)
    summer = Column(Text)
    autumn = Column(Text)
    spring = Column(Text)

class Pereval(Base):
    __tablename__ = 'pereval'
    id = Column(Integer, primary_key=True)
    beauty_title = Column(Text)
    title = Column(Text)
    other_titles = Column(Text)
    connect = Column(Text)
    add_time = Column(DateTime, default=datetime.utcnow)
    status = Column(Text, default="new")
    user_id = Column(Integer, ForeignKey('users.id'))
    coords_id = Column(Integer, ForeignKey('coords.id'))
    level_id = Column(Integer, ForeignKey('levels.id'))
    
    user = relationship("User", back_populates="perevals")
    coords = relationship("Coords")
    level = relationship("Level")
    images = relationship("Image", back_populates="pereval")

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    img = Column(LargeBinary)
    date_added = Column(DateTime, default=datetime.utcnow)
    pereval_id = Column(Integer, ForeignKey('pereval.id'))
    pereval = relationship("Pereval", back_populates="images")
