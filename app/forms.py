from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class ErrorsMessages():
    dataRequired = 'To pole nie moze byc puste'

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired(message = ErrorsMessages.dataRequired)])
    remember_me = BooleanField('remember_me', default=False)

class Testowy(Form):
    name = StringField('name', validators=[DataRequired(message = ErrorsMessages.dataRequired), Length(min=2, max=20)])