from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def landing_page():
    return render_template('home.html')


@app.route("/about")
def about_wfmh():
    return 'Work From My Home information page'


@app.route("/profile/<username>")
def profile_page(username):
    return f"This is {username}'s Work From My Home profile page"
