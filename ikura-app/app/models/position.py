#!/usr/bin/python3
"""this module creates a single class position"""
from . import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Position(Base):
    """initializes class positions and maps into table positions"""
    __tablename__ = 'positions'

    post = Column(String(50), primary_key=True)

    # relationship with candidates
    positions = relationship("Candidate", cascade="all,delete")
