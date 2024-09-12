from flask import Blueprint
from ..Controllers import product_controllers

app = Blueprint ('products',__name__)

# Admin
app.route("/products/view", methods=["POST", "GET"])(product_controllers.view_products)
app.route("/products/add", methods=["POST", "GET"])(product_controllers.add_products)


# Client 