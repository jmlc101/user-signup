from flask import Flask, render_template, request, redirect
from validate_input import validate_input

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    return validate_input(username, password, verify, email)
   
app.run()