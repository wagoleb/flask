from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class Testowy(Form):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])