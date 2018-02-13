from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ErrorsMessages():
    dataRequired = 'To pole nie moze byc puste'
    wrongEmail = 'To nie jest email'
    emailNotConfirmed = 'To nie jest ten sam email'

class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    remember_me = BooleanField('remember_me', default=False)

class Testowy(Form):
    name = StringField('name', validators = [DataRequired(message = ErrorsMessages.dataRequired), Length(min=2, max=20)])
    email = StringField('email', validators = [DataRequired(message = ErrorsMessages.dataRequired), Email(message = ErrorsMessages.wrongEmail)])
    confirmEmail = StringField('confirmEmail', validators = [DataRequired(ErrorsMessages.dataRequired), EqualTo('email', ErrorsMessages.emailNotConfirmed)])

class Login(FlaskForm):
    username = StringField('Username', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    password = PasswordField('Password', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
