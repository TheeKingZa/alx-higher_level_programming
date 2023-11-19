#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State object
    new_state = State(name='California')

    # Create the City object
    new_city = City(name='San Francisco')

    # Associate the City with the State using the relationship
    new_state.cities.append(new_city)

    # Add only the State to the session (SQLAlchemy will cascade the changes)
    session.add(new_state)

    # Commit the changes to the database
    session.commit()
