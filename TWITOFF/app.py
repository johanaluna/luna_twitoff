"""Main application for twitoff"""

#imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

def create_app():
    """create and configures an instance of a flask app"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['ENV'] = 'debug'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    return app
