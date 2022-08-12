import flask

from . import auth


@auth.route('/login/')
def login():
    return flask.render_template('auth/login.html')


@auth.route('/signup/')
def signup():
    return flask.render_template('auth/signup.html')


@auth.route('/profile/')
def profile():
    return flask.render_template('auth/profile.html')