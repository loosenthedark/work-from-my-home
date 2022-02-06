import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
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

from wfmh import routes
