import flask
import flask_login
from flask_login import login_required, current_user

from .forms import SignUp, SignIn
from app import db, login_manager
from app.models import User

from . import auth


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('auth.profile'))

    form = SignIn()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(form.password.data):
            return flask.redirect(flask.url_for('main.index'))

        flask.flash('Username or password is invalid')

    if form.errors:
        error = list(form.errors.values())[0][0]
        flask.flash(error)

    return flask.render_template('auth/signin.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('auth.profile'))

    form = SignUp()

    if form.validate_on_submit():
        username_is_taken = User.query.filter_by(username=form.username.data).first()
        email_is_taken = User.query.filter_by(email=form.email.data).first()

        if username_is_taken:
            flask.flash("Username is already taken")
        elif email_is_taken:
            flask.flash("Email is already taken")
        else:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
                               )
            db.session.add(user)
            db.session.commit()

            flask_login.login_user(user)
            return flask.redirect(flask.url_for('main.index'))

    if form.errors:
        error = list(form.errors.values())[0][0]
        flask.flash(error)

    return flask.render_template('auth/signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    flask_login.logout_user()
    flask.flash('You have been logged out')
    return flask.redirect(flask.url_for('main.index'))


@auth.route('/profile/')
@login_required
def profile():
    return flask.render_template('auth/profile.html')