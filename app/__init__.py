import flask
import flask_sqlalchemy
import flask_login
import flask_marshmallow

from config import configs


db = flask_sqlalchemy.SQLAlchemy()
login_manager = flask_login.LoginManager()
marshmallow = flask_marshmallow.Marshmallow()


def create_app(config_name: str):
    app = flask.Flask(__name__)
    app.config.from_object(configs[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    marshmallow.init_app(app)

    from .main import main as main_bp
    from .auth import auth as auth_bp
    from .timetable import timetable as timetable_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(timetable_bp)

    return app