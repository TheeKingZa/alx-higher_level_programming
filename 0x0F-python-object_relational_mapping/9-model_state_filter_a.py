#!/usr/bin/python3
"""
Prints State objects from the database hbtn_0e_6_usa that contain the letter 'a'.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State objects from the table that contain the letter 'a' in their name
    for instance in session.query(State).filter(State.name.like('%a%')):
        # Print the id and name attributes of each matching State object
        print(instance.id, instance.name, sep=": ")

    # Close the session
    session.close()
