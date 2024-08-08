from .. import mongo

from .. import mongo

class User:

    # User Login & Register
    def add_user_to_db(user_data):
        return mongo.db.user.insert_one(user_data)
    
    # Fix
    def login_user(email, password):
         mongo.db.admin.find_one(email, password)
         return str() 

     # Admin Login & Register
    def add_admin_to_db(admin_data):
        return mongo.db.admin.insert_one(admin_data)
    
    # Fix
    def admin_login(admin_data):
         mongo.db.admin.find_one(admin_data)
         return str() 
       