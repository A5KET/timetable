import os

import flask_migrate

import app


app = app.create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = flask_migrate.Migrate


@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)