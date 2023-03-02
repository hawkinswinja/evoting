#!/usr/bin/python3
"""this module creates a single class Voter"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()

class Voter(Base):
    """ creates table voters and initializes voters with unique id"""
    __tablename__ = 'voters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    auth_id = Column(String(50), default=str(uuid.uuid4()))
    status = Column(String(200), default='')

