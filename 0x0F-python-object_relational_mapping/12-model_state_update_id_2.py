#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database.
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

    # Query the State object with id 2 from the table
    new_instance = session.query(State).filter_by(id=2).first()

    # Update the name of the queried State object
    new_instance.name = 'New Mexico'

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
