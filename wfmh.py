from flask import Flask

app = Flask(__name__)


@app.route("/")
def landing_page():
    return 'Welcome to Work From My Home!'
