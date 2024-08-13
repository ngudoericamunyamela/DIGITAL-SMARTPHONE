from flask import render_template, request, url_for, redirect,flash
from ..Models.user_models import User

def landing():
    return render_template("landingpage.html")

def signup():
    if request.method == "POST":
        # Declare variables
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Add user to the database
        admin_data = {'name': name, 'email': email, 'password': password}
        
        # If user is successfully added to the database
        if User.find_by_username_and_password(admin_data):  # Ensure this method exists and works
            return redirect(url_for('user.admin_login'))  # Redirect to admin login or another page
        else:
            # Handle failure to add user (optional)
            return "Error: User not added", 500
    else:
        # Render the signup page if the request method is not POST
        return render_template("adminsignup.html")

def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user_data = {"email": email, "password": password}
        user = User.login(user_data)
  
        if user:
            return redirect(url_for('user.products'))  # Redirect to services page or admin dashboard
        else:
            # Handle login failure
            return "Error: Invalid credentials", 401

    return render_template('adminlogin.html')

def products():
    return render_template("products.html")




def admin_signup():
    if request.method == "POST":
        # Declare variables
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Add user to the database
        admin_data = {'name': name, 'email': email, 'password': password}
        
        # If user is successfully added to the database
        if User.add_admin_to_db(admin_data):  # Ensure this method exists and works
            return redirect(url_for('user.admin_login'))  # Redirect to admin login or another page
        else:
            # Handle failure to add user (optional)
            return "Error: User not added", 500
    else:
        # Render the signup page if the request method is not POST
        return render_template("adminsignup.html")

def admin_login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user_data = {"email": email, "password": password}
        user = User.admin_login(user_data)
  
        if user:
            return redirect(url_for('user.products'))  # Redirect to services page or admin dashboard
        else:
            # Handle login failure
            return "Error: Invalid credentials", 401

    return render_template('adminlogin.html')

def products():
    return render_template("products.html")


