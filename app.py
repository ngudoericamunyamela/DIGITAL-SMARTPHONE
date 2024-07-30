
from flask import Flask
from flask import request
# from  flask_pymongo import PyMongo
from flask import render_template
from pymongo import MongoClient


app= Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['Page']
collection = db['user']
# app.config["MONGO_URI"] = "mongodb://localhost:27017/signuppage"
# Mongo = PyMongo(app)
# db = Mongo.db

  # @app.route("/",methods= ["Post","Get"])
  # def signup():
  #   render_template("index.html")
@app.route("/signup",methods= ["POST","GET"])
def signup():
    if request.method=="POST":

    #  //declere variable
       name=request.form['name']
       email=request.form['email']
       password=request.form['password']
     
# //adding user to the database
       user={'name':name ,'email':email, 'password':password}
       collection.insert_one(user)
    #   If user succefully go to login
       if user:
         "succesful"
         return render_template("login.html")
      
    return  render_template("signup.html")




# landing
@app.route('/', methods=["POST","GET"])
def landing():
   return render_template("landingpage.html")
   
    
# login app.py
@app.route('/login', methods=['POST',"GET"])
def login():
    if request.method=="POST":
       email = request.form['email']
       password = request.form['password']

       user={"email":email, "password":password}
       collection.find_one(user)
  
       if user:
          return render_template("services.html")
       
    return render_template('login.html')

@app.route('/services')
def services():
   return render_template("services.html")

if __name__ == "__main__":
  app.run(debug=True)

