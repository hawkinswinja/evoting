#!/usr/bin/python3
"""creates the table candidates"""
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from models.voter import Base


class Candidate(Base):
    """candidates vying for electoral position"""
    __tablename__ = "candidates"

    voter_id = Column(Integer, ForeignKey('voters.id', ondelete='CASCADE'), primary_key=True)
    post_id = Column(String(50), ForeignKey('positions.post'))

    details = relationship("Voter")
