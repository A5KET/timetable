from re import L
import flask
import flask_wtf
import wtforms as wtf
from wtforms import validators as vld


from app import models


class SignUp(flask_wtf.FlaskForm):
    username = wtf.StringField('username', validators=[
        vld.InputRequired(), 
        vld.Length(6, 20), 
        vld.Regexp(r'^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores'),
    ])

    email = wtf.EmailField('email', validators=[vld.InputRequired(), vld.Email()])
    password = wtf.PasswordField('password', validators=[vld.InputRequired(), vld.Length(6)])
    submit = wtf.SubmitField('SIGN UP')

    def validate_username(self, field):
        if models.User.query.filter_by(username=field.data).first():
            raise wtf.ValidationError

    def validate_email(self, field):
        if models.User.query.filter_by(email=field.data).first():
            raise wtf.ValidationError


class Login(flask_wtf.FlaskForm):
    username = wtf.StringField('username', validators=[
        vld.InputRequired(),
        vld.Length(6, 20)
        ])

    password = wtf.PasswordField('password', validators=[vld.Length(6, message='Invalid password')])
    submit = wtf.SubmitField('LOGIN')