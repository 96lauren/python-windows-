#!flask/Source/python 
import mysql.connector
from  flask import Flask
from mysql.connector import errorcode 

try:
  connection= mysql.connector.connect(
	host= 'localhost',
	user='root',
	password= '',
	database='todo_list',

	)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  connection.close()
app = Flask ('app')
@app.route('/') 



def index():
	return 'Miss me?'


 

if __name__ == '__main__': 
	app.run(debug=True)

