# Interact with our database.
import psycopg2
from psycopg2 import pool


# Connect to the DB(user, password, database name, location of the database(server where its running))

# Create a Connection Pool as a class to SAVE EXPENSIVE time from creating multiple connections.
# A connection pool is when you open up multiple connections to the database, so that when sending or...
# ...retrieving data is required one of the connections can be used.
# That way there is no need to open connections, as that is expensive in terms of the time it takes.


class Database:  # We make the connection pool into a class so we can call it when we need it...
                 #  ...and it doesnt automatically get executed.
    __connection_pool = None  # __<variable name> creates a private variable


    @classmethod
    # The CONNECTION_POOL property will initially have no value, once we execute  the initialise method...
    # ...we will give the CONNECTION_POOL property the value passed to the initialise method from app.py
    def initialise(cls, **kwargs):  # **kwargs means allow any number of named variables
        cls.__connection_pool = pool.SimpleConnectionPool(minconn=1,
                                                          # Minimum allowable connections at any given time
                                                          maxconn=10,
                                                          # Maximum allowable connections at any given time
                                                          **kwargs)

    @classmethod
    def get_connection(cls):  # cls = Database
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)
        # Connection Object is automatically...
        # ... generated when we establish a connection to our DB.
        # <connection object at 0x0000017B0419F040; dsn: 'user=postgres password=xxx dbname=learning host=localhost', closed: 0>
        # i.e. connection = psycopg2.connect(database='my_database_name')
        # print(connection.dsn) OUTPUT: dbname=my_database_name


    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


# Creating a ConnectionPool class

class CursorFromConnectionFromPool:
    def __init__(self):
        # Create a Connection Property
        # Everytime we create a ConnectionFromPool object, the connection that it represents is None.
        self.connection = None
        self.cursor = None  # Initialize a new cursor

    def __enter__(self):
        # Enter INTO the 'with' clause
        # When we call the __enter__ method at the beginning of the 'with' clause,...
        # ... it will get a new connection from the Connection Pool and return that connection.
        self.connection = Database.get_connection()  # Get a Connection from the Connection Pool
        self.cursor = self.connection.cursor()  # Get a Cursor from the Connection
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:  # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback()  # If their is an error, roll the connection back...
        # ... (Undo whatever caused the error)
        else:
            # What happens when we EXIT the 'with' clause
            # Return the connections to the Connection Pool
            self.cursor.close()  # Close Cursor then commit to the connection
            self.connection.commit()  # Commit connection before closing, to save to DB
        Database.return_connection(self.connection)
