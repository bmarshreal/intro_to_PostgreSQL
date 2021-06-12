# Interact with our database.
import psycopg2
from psycopg2 import pool

# Connect to the DB(user, password, database name, location of the database(server where its running))

# Create a Connection Pool class


class Database:
    connection_pool = None

    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(minconn=1,
                                                             # Minimum allowable connections at any given time
                                                             maxconn=10,
                                                             # Maximum allowable connections at any given time
                                                             user='postgres',
                                                             password='SuperKade@061490',
                                                             database='learning',
                                                             host='localhost')

    @classmethod
    def get_connection(cls):  # cls = Database
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()


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
