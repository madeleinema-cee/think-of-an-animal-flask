from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bd95b20cb68c470de174216f1ead5b9c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
question = []
db = SQLAlchemy(app)

from flaskgame import routes
