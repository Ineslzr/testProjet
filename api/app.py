from distutils.log import debug
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


 #Members API route
@app.route("/")
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    fetchdata = cur.fetchall()
    cur.close()
    return {"Home": [fetchdata]}


@app.route("/members")
def members():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    fetchdata = cur.fetchall()
    cur.close()
    return {"members": [fetchdata]}

if __name__ == "__main__":
    app.run(debug=True)