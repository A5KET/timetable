import os
import dotenv 


dotenv.load_dotenv('.env')


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


configs = {
    'dev': DevConfig,
    'prod': ProdConfig
}

