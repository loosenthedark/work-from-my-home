import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
app.config[
    'SECRET_KEY'] = os.environ.get(
        'SECRET_KEY')

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from wfmh import routes
