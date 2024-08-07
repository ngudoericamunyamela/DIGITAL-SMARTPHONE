from flask import render_template, request, url_for, redirect
from ..Models.user_models import services
from bson.objectid import*

def update_service():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]

    # Update service in MongoDB

    # Redirect to the home page after updating service
        return render_template("Update.html", id=id)


def update_service2():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]
        categories = request.form["categories"]
        price = request.form["price"]
        colour = request.form["colour"]
        description = request.form["description"]
    
        return render_template("Update.html", id=id)

def delete_Display_Services():
    if request.method == "POST":
        # Get form data
        id = request.form["delete_id"]

       
        return render_template("Display_Services.html", services=services)

    return render_template("Add_Services.html")