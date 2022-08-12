import flask

auth = flask.Blueprint('auth', __name__)

from . import views