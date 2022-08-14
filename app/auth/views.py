import flask

from .forms import SignUp, Login
from app import models
from app import db

from . import auth


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        pass
        # TODO user_authenitification

    return flask.render_template('auth/login.html', form=form)


@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        user = models.User(
            username=form.username.data, 
            email=form.email.data, 
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()

        return flask.render_template('auth/profile.html')

    return flask.render_template('auth/signup.html', form=form)


@auth.route('/profile/')
def profile():
    return flask.render_template('auth/profile.html')