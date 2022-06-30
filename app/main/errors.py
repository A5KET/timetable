import flask

from . import main_blueprint


@main_blueprint.app_errorhandler(404)
def page_not_found(error):
    print(error)
    return flask.render_template('404.html'), 404


@main_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500