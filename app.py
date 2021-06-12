# The main app.
from database import Database
from user import User
from database import Database

Database.initialise(database='learning', host='localhost', user='postgres', password='SuperKade@061490')  # Initialize Database

user = User('yoyoyo@yahoo.com', 'yo', 'yo', None)  # Write to DB

user.save_to_db()  # Commit to DB

user_from_db = User.load_from_db_by_email('yoyoyo@yahoo.com')  # Retrieve from DB

print(user_from_db)  # Print retrieved data from DB



# print(Database.connection_pool)

# Database.initialise()

# print(Database.connection_pool)
