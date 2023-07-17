#!/usr/bin/python3
"""this module creates a single class Voter"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Voter(Base):
    """ creates table voters and initializes voters with unique id"""
    __tablename__ = 'voters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(15))
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    auth_id = Column(String(100), nullable=False)
