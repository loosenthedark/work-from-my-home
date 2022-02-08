import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import create_engine
from wfmh import routes
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

DATABASE_CONNECTION = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')
engine = create_engine(DATABASE_CONNECTION, pool_size=50, max_overflow=100)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'wfmh_login'
login_manager.login_message_category = 'warning'
