from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key='secretshhh'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'login')
PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")

@app.route('/')
def index():
    if 'login' not in session:
        session['login'] = False
    if session['login'] == True:
        return render_template('success.html')
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session['login'] = False
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print 'test'
    data = {
        "email": request.form['email'],
        "password": request.form['pwd']
    }
    for ele in data.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n')
            return redirect('/')

    
    query = "SELECT user.email, user.password FROM user WHERE email = :email"
    print query
    login_user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(login_user[0]['password'], data['password']):
        session['login'] = True
    return redirect('/')

@app.route('/process', methods=['POST'])
def process():
    data = {
        "email": request.form['email'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "password": request.form['pwd'],
        "pwd_confirm": request.form['pwd2']
    }

    for ele in data.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n', 'red')
    if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', data['email']):
        flash('Invalid Email!')
    
    if data['password'] != data['pwd_confirm']:
        flash('Password does not match!')
    
    if not PASSWORD_REGEX.match(data['password']):
        flash('Password must be a minimum of 8 characters and at least 1 Alphabet and 1 Number')
    
    if '_flashes' not in session:
        session['login'] = True
        data['password'] = bcrypt.generate_password_hash(data['password'])
        query = "INSERT INTO user (fname, lname, email, password, created_at, updated_at) VALUES (:fname, :lname, :email, :password ,NOW(), NOW())"
        mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
