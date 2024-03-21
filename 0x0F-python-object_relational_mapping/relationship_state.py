#!/usr/bin/python3
"""
a Python file similar to model_state.py named relationship_state.py
that contains the class definition of a State.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class inherits from Base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state", cascade="all, delete")
