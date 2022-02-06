from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def landing_page():
    return render_template('home.html')


@app.route("/browse")
def browse_homes():
    homes = [
        {'id': 1, 'description': 'city centre studio', 'location': 'Dublin 2', 'identifier': '123456789', 'daily_rate': 100},
        {'id': 2, 'description': 'terraced redbrick close to Luas', 'location': 'Dublin 8', 'identifier': '987654321', 'daily_rate': 85},
        {'id': 3, 'description': 'quiet bungalow; pet-friendly', 'location': 'Wicklow', 'identifier': '693047511', 'daily_rate': 70},
        {'id': 4, 'description': 'spacious loft apartment; available Mon-Wed', 'location': 'Dublin 1', 'identifier': '964827400', 'daily_rate': 140},
        {'id': 5, 'description': 'bright, newly-renovated home office', 'location': 'Kildare', 'identifier': '830495118', 'daily_rate': 90}
        ]
    return render_template('browse.html', homes=homes)


@app.route("/about")
def about_wfmh():
    return 'Work From My Home information page'


@app.route("/profile/<username>")
def profile_page(username):
    return f"This is {username}'s Work From My Home profile page"
