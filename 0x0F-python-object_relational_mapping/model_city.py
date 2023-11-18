#!/usr/bin/python3
"""
Module that defines the City class, which is a SQLAlchemy model
representing the 'cities' table in the database.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class representing the 'cities' table in the database.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): Unique identifier for each city.
        name (str): The name of the city.
        state_id (int):
            Foreign key referencing the 'id'
            column in the 'states' table.
    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
