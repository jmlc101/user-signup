from flask import Flask, render_template, request, redirect
import re

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
    name_error_msg = "That's not a valid username"
    pass_error_msg = "That's not a valid password"
    nonmatch_error = "Passwords do not match"
    email_err = "That's not a valid email"

    if password == '':
        password = ' '
    if verify == '':
        verify = ' '
    if username == '':
        username = ' '
    

    tple = username, password, verify
    string = ' '.join(tple)
    tple2 = username, password
    string2 = ' '.join(tple2)
    regex2 = r"([\w\W]+) ([\w\W]+)"
    regex3 = r"([\w\W]+) ([\w\W]+) ([\w\W]+)"
    email_regex = r"^\w+@\w+\.\w+$"
    regex = re.compile(r"\w{3,20}")
    grps = re.search(regex3, string)
    grps2 = re.search(regex2, string2)

    if regex.search(grps.group(1)) and regex.search(grps.group(2)) and (password == verify):
        if (regex.search(email) and re.search(email_regex, email)) or (email == ''):
            return render_template("welcome.html", name=username)
        else:
            return render_template("signup.html", email_error=email_err, name=username)
    elif regex.search(grps2.group(1)) and regex.search(grps2.group(2)):
        if (regex.search(email) and re.search(email_regex, email)) or (email == ''):
            return render_template("signup.html", email=email, name=username, verify_pass_error=nonmatch_error)
        else:
            return render_template("signup.html", name=username, verify_pass_error=nonmatch_error, email_error=email_err)
    elif regex.search(username):
        if (regex.search(email) and re.search(email_regex, email)) or (email == ''):
            return render_template("signup.html", email=email, name=username, pass_error=pass_error_msg)
        else:
            return render_template("signup.html", name=username, pass_error=pass_error_msg, email_error=email_err)
    elif (password == ' ') and (verify == ' ') and (username == ' '):
        if (regex.search(email) and re.search(email_regex, email)) or (email == ''):
            return render_template("signup.html", email=email, user_name_error=name_error_msg, pass_error=pass_error_msg)
        else:
            return render_template("signup.html", user_name_error=name_error_msg, pass_error=pass_error_msg, email_error=email_err)

app.run()