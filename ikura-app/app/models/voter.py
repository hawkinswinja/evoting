#!/usr/bin/python3
"""this module creates a single class Voter"""
from . import Base
from sqlalchemy import Column, String, Integer, Boolean

class Voter(Base):
    """ Table for voters with additional user category """

    __tablename__ = 'voters'


    voter_id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(100), default='Not') # voted status
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    auth_id = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)