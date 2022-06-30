import flask
import flask_sqlalchemy


db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = flask.Flask(__name__)

    db.init_app(app)

    from .main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app