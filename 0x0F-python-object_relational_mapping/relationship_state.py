#!/usr/bin/python3
"""
Module that defines the State class, which is a SQLAlchemy model
representing the 'states' table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class representing the 'states' table in the database.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): Unique identifier for each state.
        name (str): The name of the state.
        cities (relationship): Relationship with the City class.
    """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state", cascade="all, delete-orphan"
            )
