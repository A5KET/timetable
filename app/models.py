from . import db


class Info(db.Model):
    __tablename__ = 'info'
    id  = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    

class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    