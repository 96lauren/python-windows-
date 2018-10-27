#!flask/Source/python 
from  flask import Flask, jsonify,request
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

config = Config()
cursor=config.get_cursor()
app = Flask ('app')

@app.route('/')
def index():
	return 'Miss me ?'

@app.errorhandler(404)
def page_not_found(error):
  result={
  "statusCode":404,
  "status":"failed",
  "message":"NOT FOUND"
  }
  return jsonify(result)


@app.route('/user',methods=['GET']) 
def get_users(): 
  
  cursor.execute("SELECT * FROM user")
  user_data = cursor.fetchall()
  result={
  "result":user_data
  }

  return jsonify (result) 


@app.route('/register', methods=['POST'])
def register_user():
  result =request.get_json()
  # get data from the request object
  name= result['name']
  email = result['email']
  password= result['password']
  password_hash = generate_password_hash(password)
  # Insert data to the table 

  querry = "INSERT INTO user VALUES (%s,%s,%s,%s,NOW())"
  values =(4,name, email, password_hash)
  cursor.execute(querry,values)
  # Gt the number of rows inserted 
  row_count = cursor.rowcount
  if row_count > 0:
    result ={
    "status":"successful",
    "message":"user_created."

    }
  else:
    result = {
    "status":"failed",
    "message":"Error creating user."

    }
  return jsonify(result) 

@app.route('/login', methods=['POST'])
def login():
  post_request = request.get_json()

  email = post_request['email']
  password=post_request['password']

  password_hash =generate_password_hash(password)
  # select from DB
  query ="SELECT * FROM user WHERE 'email'=%s"
  values = (email, )
  cursor.execute(query,values)
  user_data =cursor.fetchall()

  return jsonify (user_data)


  
 

if __name__ == '__main__':
	app.run(debug=True)

