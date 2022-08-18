import flask
import flask_login
from flask_login import current_user

from .forms import SignUp, Login
from app import db, models, login_manager

from . import auth


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(models.User, user_id)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if current_user.is_authenticated:  # type: ignore
        return flask.redirect(flask.url_for('auth.profile'))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db.session.query(models.User).filter(models.User.username == username, models.User.password == password).first()
        print(user)

        if not user:
            flask.flash('Username or password is invalid')
            return flask.redirect(flask.url_for('auth.login'))

        flask_login.login_user(user)
        return flask.redirect(flask.url_for('main.index'))

    return flask.render_template('auth/login.html', form=form)


@auth.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flask.flash('You have been logged out')
    return flask.redirect(flask.url_for('main.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()

    if current_user.is_authenticated:  # type: ignore
        return flask.redirect(flask.url_for('auth.profile'))


    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = models.User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flask_login.login_user(user)

        return flask.redirect(flask.url_for('main.index'))

    return flask.render_template('auth/signup.html', form=form)


@auth.route('/profile/')
@flask_login.login_required
def profile():
    return flask.render_template('auth/profile.html')