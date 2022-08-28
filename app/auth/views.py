import flask
import flask_login
from flask_login import current_user

from .forms import SignUp, SignIn
from app import db, models, login_manager

from . import auth


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(models.User, user_id)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignIn()

    if current_user.is_authenticated:  # type: ignore
        return flask.redirect(flask.url_for('auth.profile'))

    if form.validate_on_submit():
        email: str = form.email.data
        password: str = form.password.data

        user: models.User | None = models.User.query.filter_by(email=email.lower()).first()
        print(user)

        if user and user.verify_password(password):
            flask_login.login_user(user)
            return flask.redirect(flask.url_for('main.index'))

        flask.flash('Username or password is invalid')

    return flask.render_template('auth/signin.html', form=form)


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