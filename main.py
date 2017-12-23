from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    encoded_error = request.args.get("name_error")
    encoded_error = request.args.get("pass_error")
    encoded_error = request.args.get("verify_pass_error")
    encoded_error = request.args.get("email_error")
    return render_template('welcome.html',  error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route("/signup", methods=['POST'])
def add_movie():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # if the user typed nothing at all, redirect and tell them the error
    if (not username) or (username.strip() == ""):
        name_error = "Please Enter a Username."
        return redirect("/?error=" + error)

    if new_movie in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_escaped = cgi.escape(new_movie, quote=True)






app.run()