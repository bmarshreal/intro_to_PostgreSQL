# The main app.
from user import User


my_user = User('bmarshreal@yahoo.com', 'Blake', 'Marshall', None)  # id will be filled by DB

# Call method from User class to SAVE TO database
my_user.save_to_db()


# my_user = User.load_from_db_by_email('bmarshreal@yahoo.com')

# Call method from User class to FETCH data FROM database by email
# my_user.load_from_db_by_email()