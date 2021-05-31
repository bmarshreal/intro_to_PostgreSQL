# store the class to model our users with.
import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email,
        self.first_name = first_name,
        self.last_name = last_name,
        self.id = id

    def __repr__(self):
        return '<User {}>'.format(self.email)  # self.email replaces {} in '<User {}>' and is printed out

    def save_to_db(self):
        # Connect to the DB(user, password, database name, location of the database(server where its running))
        with psycopg2.connect(user='postgres', password='SuperKade@061490', database='learning', host='localhost') as connection:
            # Cursor is something that lets us retrieve data and read it row by row or lets us insert data to the database.
            with connection.cursor() as cursor:
                # Running some code...Always close cursor after running a query to DB
                # Database syntax %s = string
                cursor.execute('insert into users(email, first_name, last_name)values (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))
        # Commit Connection
        connection.commit()
        # Close Connection
        connection.close()