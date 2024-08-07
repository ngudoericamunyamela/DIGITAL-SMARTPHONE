from .. import mongo

class User:

    def add_user_to_db(user_data):
        return mongo.db.user.insert_one(user_data)
    
    def  signup (user_data):
        User = mongo.db.collection.insert_one(user_data)
        return list(mongo.db.user.find({}, {'_id, 0'}))
    
    def  login (user_data):
        User = mongo.db.collection.insert_one(user_data)
        return list(mongo.db.user.find({}, {'_id, 0'}))
    

    def  admin_signup_get (user_data):
        User = mongo.db.admin_user.insert_one(user_data)
        return list(mongo.db.admin_user.find({}, {'_id, 0'}))
    
    def  admin_login_get (user_data):
        User = mongo.db.admin_user.insert_one(user_data)
        return list(mongo.db.admin_user.find({}, {'_id, 0'}))

    