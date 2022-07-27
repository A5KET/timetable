import unittest

import flask

import app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        app.db.create_all()

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()
        print(self.app_context)
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(flask.current_app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(flask.current_app.config['TESTING'])
