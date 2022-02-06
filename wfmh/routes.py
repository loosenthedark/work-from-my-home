from flask import render_template
from wfmh import app
from wfmh.forms import WFMHRegistrationForm
from wfmh.models import Home

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


@app.route("/register")
def wfmh_registration():
    r_form = WFMHRegistrationForm()
    return render_template('register.html', form=r_form)
