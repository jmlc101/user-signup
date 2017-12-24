from flask import Flask, render_template, request, redirect
from password_is_valid import password_is_valid
from username_is_valid import username_is_valid
from verify_pass import verify_pass
from email_is_valid import email_is_valid
import cgi

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
  
    if email == '':
        if username_is_valid(username) == False:
            if password_is_valid(password) == False:
                return render_template("signup.html", user_name_error=name_error_msg, pass_error=pass_error_msg)
            elif password_is_valid(password):
                if verify_pass(password, verify) == False:
                    return render_template("signup.html", user_name_error=name_error_msg, verify_pass_error=nonmatch_error)
                elif verify_pass(password, verify):
                    return render_template("signup.html", user_name_error=name_error_msg)
        elif username_is_valid(username):
            if password_is_valid(password) == False:
                return render_template("signup.html", name=username, pass_error=pass_error_msg)
            elif password_is_valid(password):
                if verify_pass(password, verify) == False:
                    return render_template("signup.html", name=username, verify_pass_error=nonmatch_error)
                elif verify_pass(password, verify):
                    return render_template("welcome.html", name=username)
    else:
        if email_is_valid(email):
            if username_is_valid(username) == False:
                if password_is_valid(password) == False:
                    return render_template("signup.html", email=email, user_name_error=name_error_msg, pass_error=pass_error_msg)
                elif password_is_valid(password):
                    if verify_pass(password, verify) == False:
                        return render_template("signup.html", email=email, user_name_error=name_error_msg, verify_pass_error=nonmatch_error)
                    elif verify_pass(password, verify):
                        return render_template("signup.html", email=email, user_name_error=name_error_msg)
            elif username_is_valid(username):
                if password_is_valid(password) == False:
                    return render_template("signup.html", email=email, name=username, pass_error=pass_error_msg)
                elif password_is_valid(password):
                    if verify_pass(password, verify) == False:
                        return render_template("signup.html", email=email, name=username, verify_pass_error=nonmatch_error)
                    elif verify_pass(password, verify):
                        return render_template("welcome.html", name=username)
        elif email_is_valid(email) == False:
            if username_is_valid(username) == False:
                if password_is_valid(password) == False:
                    return render_template("signup.html", email_error=email_err, user_name_error=name_error_msg, pass_error=pass_error_msg)
                elif password_is_valid(password):
                    if verify_pass(password, verify) == False:
                        return render_template("signup.html", email_error=email_err, user_name_error=name_error_msg, verify_pass_error=nonmatch_error)
                    elif verify_pass(password, verify):
                        return render_template("signup.html", email_error=email_err, user_name_error=name_error_msg)
            elif username_is_valid(username):
                if password_is_valid(password) == False:
                    return render_template("signup.html", email_error=email_err, name=username, pass_error=pass_error_msg)
                elif password_is_valid(password):
                    if verify_pass(password, verify) == False:
                        return render_template("signup.html", email_error=email_err, name=username, verify_pass_error=nonmatch_error)
                    elif verify_pass(password, verify):
                        return render_template("signup.html", name=username, email_error=email_err)

app.run()