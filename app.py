# The main app.
from user import User


my_user = User('bmarshreal@yahoo.com', 'Blake', 'Marshall', None)  # id will be filled by DB

my_user.save_to_db()
print(str(my_user))