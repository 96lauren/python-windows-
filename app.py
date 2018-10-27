#!flask/Source/python 
from  flask import Flask, jsonify,request
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
  result = cursor.fetchall()

  return jsonify (result) 


@app.route('/register', methods=['POST'])
def register_user():
  result =request.get_json()
  # get data from the request object
  name= result['name']
  email = result['email']
  password= result['password']
  # Insert data to the table 

  querry = "INSERT INTO user VALUES (%s,%s,%s,%s,NOW())"
  values =(3,name, email, password)
  cursor.execute(querry,values)
  return jsonify(result) 


 

if __name__ == '__main__':
	app.run(debug=True)

