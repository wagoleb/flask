from app.models import User
from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class ErrorsMessages():
    dataRequired = 'To pole nie moze byc puste'
    wrongEmail = 'To nie jest email'
    emailNotConfirmed = 'To nie jest ten sam email'
    passwordretype = 'Hasla sa rozne'


class LoginForm(FlaskForm):
    openid = StringField('openid', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    remember_me = BooleanField('remember_me', default=False)


class Testowy(FlaskForm):
    name = StringField('name', validators = [DataRequired(message = ErrorsMessages.dataRequired), Length(min=2, max=20)])
    email = StringField('email', validators = [DataRequired(message = ErrorsMessages.dataRequired), Email(message = ErrorsMessages.wrongEmail)])
    confirmEmail = StringField('confirmEmail', validators = [DataRequired(ErrorsMessages.dataRequired), EqualTo('email', ErrorsMessages.emailNotConfirmed)])


class Login(FlaskForm):
    username = StringField('Username', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    password = PasswordField('Password', validators = [DataRequired(message = ErrorsMessages.dataRequired)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message = ErrorsMessages.dataRequired)])
    email = StringField('Email', validators=[DataRequired(message = ErrorsMessages.dataRequired), Email(message = ErrorsMessages.wrongEmail)])
    password = PasswordField('Password', validators=[DataRequired(message = ErrorsMessages.dataRequired)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(message = ErrorsMessages.dataRequired), EqualTo('password', message = ErrorsMessages.passwordretype)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')