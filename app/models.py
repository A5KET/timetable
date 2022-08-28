import sqlalchemy as sql
import flask_login
from werkzeug import security

from . import db


class User(flask_login.UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) 

    table_info = db.relationship('Timetable')


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password')

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = security.generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return security.check_password_hash(self.password_hash, password)


class Timetable(db.Model):
    __tablename__ = 'timetable'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(64))
    url = db.Column(db.String(64))

    week = db.relationship('Week')


class Week(db.Model):
    __tablename__ = 'week'

    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('timetable.id'))

    week_number = db.Column(db.Integer) # <4

    day = db.relationship('Day')


class Weekday(db.Model):
    __tablename__ = 'weekday'

    id = db.Column(db.Integer, primary_key=True)
    weekday = db.Column(db.String())

    day = db.relationship('Day')


class Day(db.Model):
    __tablename__ = 'day'

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))
    weekday_id = db.Column(db.Integer, db.ForeignKey('weekday.id'))

    event = db.relationship('Event')


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    name = db.Column(db.String(32))
    description = db.Column(db.String(256))
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time) 

