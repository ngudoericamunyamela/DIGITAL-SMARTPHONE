from flask import render_template, request, url_for, redirect
from ..Models.product_model import Prod
from bson.objectid import*



# Get And View All Our Products
def view_products():
    all_products = list(Prod.get_all_products())
    return render_template("products.html", products=all_products)


# Add Products
def add_products():
    if request.method == "POST":
      
      name = request.form.get("name")
      price = request.form.get("price")
      description = request.form.get("description")
      image = request.form.get("image")

      product_info = {
         "name": name,
         "price": price,
         "description": description,
         "image": image
      }

      Prod.add_products_db(product_info)

      return redirect(url_for("products.view_products"))

    return render_template("addproducts.html")

