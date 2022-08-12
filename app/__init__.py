import flask
import flask_sqlalchemy

from config import configs


db = flask_sqlalchemy.SQLAlchemy()


def create_app(config_name: str):
    app = flask.Flask(__name__)
    app.config.from_object(configs[config_name])

    db.init_app(app)

    from .main import main as main_bp
    from .auth import auth as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app