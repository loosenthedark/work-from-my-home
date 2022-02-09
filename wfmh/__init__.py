import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
app.config[
    'SECRET_KEY'] = os.environ.get(
        'SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'wfmh_login'
login_manager.login_message_category = 'warning'

from wfmh import routes
