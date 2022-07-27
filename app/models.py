import sqlalchemy as sql

from . import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)

    user_login = db.Column(db.String(20))
    user_password = db.Column(db.String(20)) # 8 <= password <= 20
    user_email = db.Column(db.String(256))

    table_info = db.relationship('Table')


class Table(db.Model):
    __tablename__ = 'table'

    table_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    table_name = db.Column(db.String(64))
    table_url = db.Column(db.String(64))

    week = db.relationship('Week')


class Week(db.Model):
    __tablename__ = 'week'

    week_id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.table_id'))
    week_number = db.Column(db.Integer) # <4

    day = db.relationship('Day')


class Day(db.Model):
    __tablename__ = 'day'

    day_id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('week.week_id'))
    weekday = db.Column(db.Enum('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'))

    event = db.relationship('Event')



class Event(db.Model):
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.day_id'))
    event_name = db.Column(db.String(32))
    event_start = db.Column(db.Time)
    event_end = db.Column(db.Time)