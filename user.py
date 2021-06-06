# Store the class to model our users with.
import psycopg2
from database import connection_pool

# Define a class to insert into database as a table later in PostgreSQL
class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email,
        self.first_name = first_name,
        self.last_name = last_name,
        self.id = id

    def __repr__(self):
        return '<User {}>'.format(self.email)  # self.email replaces {} in '<User {}>' and is printed out

    # INSERTING DATA INTO POSTGRESQL
    def save_to_db(self):  # Create our method to fetch data from DB
        connection = connection_pool.getconn()  # Connect to DB from connection pool and close connect after method 'save_to_db' is finished
         # Cursor is something that lets us retrieve data and read it row by row or lets us insert data to the database.
        with connection.cursor() as cursor:  # Create a cursor to navigate through DB
            # Running some code...Always close cursor after running a query to DB
            # Database syntax %s = string
            cursor.execute('INSERT INTO users(email, first_name, last_name)values (%s, %s, %s)',  # Execute SQL
                               (self.email, self.first_name, self.last_name))
        connection_pool.putconn(connection)  # Re-establish a connection for the next method to run


    # RETRIEVING DATA FROM POSTGRESQL

    @classmethod
    def load_from_db_by_email(cls, email):  # Create our method to fetch data from DB
        connection = connection_pool.getconn()  # Connect to DB from connection pool
        with connection.cursor() as cursor:  # Create a cursor to navigate through DB
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))  # Execute SQL
            user_data = cursor.fetchone()  # Execute Cursor method
            # cls refers to User. Returning User.email=user_data[1], User.first_name=user_data[2], User.last_name=user_data[3], User.id=user_data[0]
            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])  # Return data from DB

# Commit Connection
# connection.commit()
# Close Connection
# connection.close()