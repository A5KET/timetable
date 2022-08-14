import os

from flask_migrate import Migrate

import app
from app import db


app = app.create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)