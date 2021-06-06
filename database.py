# Interact with our database.
import psycopg2


def connect():
    # Connect to the DB(user, password, database name, location of the database(server where its running))
    return psycopg2.connect(user='postgres', password='SuperKade@061490', database='learning', host='localhost')