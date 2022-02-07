from flask import flash, redirect, render_template, url_for
from wfmh import app, db
from wfmh.forms import WFMHLoginForm, WFMHRegistrationForm
from wfmh.models import Home, Worker

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


@app.route("/register", methods=['GET', 'POST'])
def wfmh_registration():
    r_form = WFMHRegistrationForm()
    if r_form.validate_on_submit():
        successfully_registered_user = Worker(profile_name=r_form.r_profile_name.data, worker_email=r_form.r_email.data, make_password_secure = r_form.r_password.data)
        db.session.add(successfully_registered_user)
        db.session.commit()
        return redirect(url_for('browse_homes'))

    if r_form.errors != {}:
        for error_message in r_form.errors.values():
            flash(f'There was a problem with your registration attempt: {error_message}', category='danger')

    return render_template('register.html', form=r_form)


@app.route("/login", methods=['GET', 'POST'])
def wfmh_login():
    l_form = WFMHLoginForm()
    # if r_form.validate_on_submit():
    #     successfully_registered_user = Worker(profile_name=r_form.r_profile_name.data,
    #                                           worker_email=r_form.r_email.data, make_password_secure=r_form.r_password.data)
    #     db.session.add(successfully_registered_user)
    #     db.session.commit()
    #     return redirect(url_for('browse_homes'))

    # if r_form.errors != {}:
    #     for error_message in r_form.errors.values():
    #         flash(
    #             f'There was a problem with your registration attempt: {error_message}', category='danger')

    return render_template('login.html', form=l_form)
