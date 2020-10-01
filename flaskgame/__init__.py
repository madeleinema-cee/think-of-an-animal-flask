from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret_keys['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskgame import routes
