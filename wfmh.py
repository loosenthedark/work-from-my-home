import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    summary = db.Column(db.String(length=50), nullable=False, unique=True)
    location = db.Column(db.String(length=25), nullable=False)
    owner_email = db.Column(db.String(length=50), nullable=False)
    daily_rate = db.Column(db.Integer(), nullable=False)
    # worker = db.Column(db.Integer(), db.ForeignKey('worker.id'))

    def __repr__(self):
        return f'Home {self.id}: {self.summary}'

@app.route("/")
@app.route("/home")
def landing_page():
    return render_template('home.html')


@app.route("/browse")
def browse_homes():
    homes = Home.query.all()
    return render_template('browse.html', homes=homes)


@app.route("/about")
def about_wfmh():
    return 'Work From My Home information page'


@app.route("/profile/<username>")
def profile_page(username):
    return f"This is {username}'s Work From My Home profile page"
