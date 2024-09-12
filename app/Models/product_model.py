from ..import mongo
from bson.objectid import ObjectId

class Prod:
   
    # Add products to database 
    def add_products_db(product_info):
        return mongo.db.products.insert_one(product_info)

    # Retrieve / Get products from database
    def get_all_products():
        return mongo.db.products.find()

