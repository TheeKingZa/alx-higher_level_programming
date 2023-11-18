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

    # Create a new State object with the specified name
    new_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(new_state)

    # Query the new State object from the table
    new_instance = session.query(State).filter_by(name='Louisiana').first()

    # Print the id of the new State object
    print(new_instance.id)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
