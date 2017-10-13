from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    # year = mysql.query_db("SELECT YEAR('friendsince') FROM friends")
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name,age, friendsince) VALUES (:name, :age, NOW())"
    data = {
             'name': request.form['name'],
             'age': request.form['age']
           }
    friends= mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_name>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE name = :specific_name"
    data = {'specific_age': friend_age}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

app.run(debug=True)