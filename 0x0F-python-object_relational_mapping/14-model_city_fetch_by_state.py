#!/usr/bin/python3
"""Prints the State object with the name passed
    as an argument from the database.
"""
import sys
from model_state import Base, State
from model_city import City
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

    # Query State and City objects and filter by matching state IDs
    query = (session.query(State.name, City.id, City.name)
             .filter(State.id == City.state_id))

    # Print the results
    for instance in query:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])

    # Close the session
    session.close()
