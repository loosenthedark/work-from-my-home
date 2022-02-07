from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from wfmh import app, db
from wfmh.forms import WFMHLoginForm, WFMHRegistrationForm
from wfmh.models import Home, Worker

@app.route("/")
@app.route("/home")
def landing_page():
    return render_template('home.html')


@app.route("/browse")
@login_required
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
        login_user(successfully_registered_user)
        flash(
            f'Account created successfully! You are now logged in as {successfully_registered_user.profile_name}', category='success')
        return redirect(url_for('browse_homes'))

    if r_form.errors != {}:
        for error_message in r_form.errors.values():
            flash(f'There was a problem with your registration attempt: {error_message}', category='danger')

    return render_template('register.html', form=r_form)


@app.route("/login", methods=['GET', 'POST'])
def wfmh_login():
    l_form = WFMHLoginForm()
    if l_form.validate_on_submit():
        pre_login_user = Worker.query.filter_by(profile_name=l_form.l_profile_name.data).first()
        if pre_login_user and pre_login_user.check_password_attempt(password_attempt=l_form.l_password.data):
            login_user(pre_login_user)
            flash(f'Success! You are now logged in as {pre_login_user.profile_name}', category='success')
            return redirect(url_for('browse_homes'))
        else:
            flash(
                'That username and password do not match. Please try again!', category='danger')

    return render_template('login.html', form=l_form)


@app.route("/logout")
def wfmh_logout():
    logout_user()
    flash(
        'You have logged out successfully!', category='info')
    return redirect(url_for('landing_page'))
