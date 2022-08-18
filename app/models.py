import sqlalchemy as sql
import flask_login

from . import db


class User(flask_login.UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(20)) # TODO implement password hashing 

    table_info = db.relationship('Table')


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Table(db.Model):
    __tablename__ = 'table'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    name = db.Column(db.String(64))
    url = db.Column(db.String(64))

    week = db.relationship('Week')


class Week(db.Model):
    __tablename__ = 'week'

    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

    week_number = db.Column(db.Integer) # <4

    day = db.relationship('Day')


class Day(db.Model):
    __tablename__ = 'day'

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))

    weekday = db.Column(db.Enum('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'))

    event = db.relationship('Event')


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    name = db.Column(db.String(32))
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time) 

