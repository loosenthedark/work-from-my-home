from flask import Flask

app = Flask(__name__)


@app.route("/")
def landing_page():
    return 'Welcome to Work From My Home!'


@app.route("/about/<username>")
def about_wfmh():
    return 'Work From My Home information page'


@app.route("/profile/<username>")
def profile_page(username):
    return f"This is {username}'s Work From My Home profile page"
