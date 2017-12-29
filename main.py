from flask import Flask, render_template, request, redirect
from validate_input import validate_input
import webbrowser

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

# adapted from this stack overflow answer
# https://stackoverflow.com/a/24353812/7542831
port = 5000 # set the port you want to expose here
url = 'http://127.0.0.1:{}'.format(port)

# these are the file paths to the chrome / other browser you want to auto-open:
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows (uncomment for windows machines)
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
# Linux (uncomment for linux machines)
browser_path = '/usr/bin/firefox %s'

# this calls the webbrowser module to open the url with the given browser
webbrowser.get(browser_path).open(url)

app.run(port=port)