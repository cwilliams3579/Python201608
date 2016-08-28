from flask import Flask, render_template, redirect, request, session, flash, url_for
import re
import random

PASS_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = {
        "email": request.form['email'],
        "first name": request.form['fname'],
        "last name": request.form['lname'],
        "password": request.form['pwd'],
        "password confirmation": request.form['pwd2']
    }
    for ele in data.items():
        if len(ele[1]) < 1:
            flash(ele[0] + ' is Required. \n')
    if data['password'] != data['password confirmation']:
        flash('Password does not match!')
    if not PASS_REGEX.match(data['password']):
        flash('Password minimum 8 characters, at least 1 Alphabet and 1 Number')
    if '_flashes' not in session:
        flash('Successful!')

    return redirect("/")

app.run(debug=True)
