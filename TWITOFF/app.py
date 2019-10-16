"""Main application for twitoff"""

#imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

def create_app():
    """create and configures an instance of a flask app"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB reset', users=[])

    # @app.route('/user/<username>')
    # def profile(username):
    #     return '{}\'s profile'.format(escape(username))
    #
    # with app.test_request_context():
    #     print(url_for('index'))
    #     print(url_for('login'))
    #     print(url_for('login', next='/'))
    #     print(url_for('profile', username='John Doe'))
    return app
