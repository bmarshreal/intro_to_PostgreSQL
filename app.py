# The main app.
from user import User


my_user = User('annasmith@yahoo.com', 'Anna', 'Smith', None)  # id will be filled by DB

# Call method from User class to SAVE TO database
my_user.save_to_db()


user_from_db = User.load_from_db_by_email('annasmith@yahoo.com')
print(user_from_db)

# Call method from User class to FETCH data FROM database by email
#  my_user.load_from_db_by_email()