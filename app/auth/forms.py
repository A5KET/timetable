import flask
import flask_wtf
import wtforms as wtf
from wtforms import validators as vld


class SignUp(flask_wtf.FlaskForm):
    username = wtf.StringField('username', validators=[
        vld.InputRequired(), 
        vld.Length(6, 20), 
        vld.Regexp(r'^[!-~]+$'),
    ])

    email = wtf.EmailField('email', validators=[vld.InputRequired(), vld.Email()])
    password = wtf.PasswordField('password', validators=[vld.InputRequired(), vld.Length(6)])
    submit = wtf.SubmitField('SIGN UP')


class Login(flask_wtf.FlaskForm):
    username = wtf.StringField('username', validators=[
        vld.InputRequired(),
        vld.Length(6, 20)
        ])

    password = wtf.PasswordField('password', validators=[vld.Length(6, message='Invalid password')])
    submit = wtf.SubmitField('LOGIN')