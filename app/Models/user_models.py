from pymongo import MongoClient
from .. import mongo

class User:
    
    
    def find_user(query):
        return mongo.db.users.find_one(query)

    def insert_user(user_data):
        return mongo.db.users.insert_one(user_data)
    
    def is_user_exist(username, email):
        return mongo.db.users.find_one({'$or': [{'username': username}, {'email': email}]})


    def find_by_username_and_password(username, password):
        return mongo.db.users.find_one({'username': username, 'password': password})
    
 
    def add_admin_to_db(admin_data):
        return mongo.db.admin_register.insert_one(admin_data)
    
    def admin_login(admin_data):
        # The method should return the result of the query
        result = mongo.db.admin_register.find_one(admin_data)
        return result

       