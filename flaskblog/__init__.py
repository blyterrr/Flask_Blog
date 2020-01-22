from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '1478228fe97868c31d03c5aeebc807d2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# db instance
db = SQLAlchemy(app)

from flaskblog import routes