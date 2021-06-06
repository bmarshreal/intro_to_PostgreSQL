# Interact with our database.
import psycopg2
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn=1,  # Minimum allowable connections at any given time
                                            maxconn=10,  # Maximum allowable connections at any given time
                                            user='postgres',
                                            password='SuperKade@061490',
                                            database='learning',
                                            host='localhost')
# Connect to the DB(user, password, database name, location of the database(server where its running))
