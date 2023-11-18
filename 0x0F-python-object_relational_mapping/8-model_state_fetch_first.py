#!/usr/bin/python3
""" 
Prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object from the table
    instance = session.query(State).first()

    # Check if the object exists
    if instance is None:
        print("Nothing")
    else:
        # Print the id and name attributes of the State object
        print(instance.id, instance.name, sep=": ")

    # Close the session
    session.close()
