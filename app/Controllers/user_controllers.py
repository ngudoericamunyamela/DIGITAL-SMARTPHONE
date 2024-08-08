from flask import render_template, request, url_for, redirect
from ..Models.user_models import User


def landingpage():
   return render_template("landingpage.html")

# Signup client
def signup():
    if request.method=="POST":
    #  //declere variable
       name=request.form['name']
       email=request.form['email']
       password=request.form['password']
     
    # //adding user to the database
       user_data ={'name':name ,'email':email, 'password':password}

    #   If user succefully go to login
       if User.add_user_to_db(user_data):
         return render_template("login.html")
      
    return  render_template("signup.html")

# Login client
def login():
    if request.method=="POST":
       email = request.form['email']
       password = request.form['password']

       user_data={"email":email, "password":password}
       user = User.login(user_data)
  
       if user:
          return redirect (url_for('user.services'))
       
    return render_template('login.html')


def admin_signup():
    if request.method=="POST":
    #  //declere variable
       name=request.form['name']
       email=request.form['email']
       password=request.form['password']
     
    # //adding user to the database
       user_data ={'name':name ,'email':email, 'password':password}

    #   If user succefully go to login
       if User.admin_signup_get(user_data):
     
      
         return  render_template("adminsignup.html")

def admin_login():
    if request.method=="POST":
       email = request.form['email']
       password = request.form['password']

       user_data={"email":email, "password":password}
       user = User.admin_login_get(user_data)
  
       if user:
       
       
        return render_template('adminlogin.html')



def landing():
   return render_template("landingpage.html")

def services():
   return render_template("services.html")

