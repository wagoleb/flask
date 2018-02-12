from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, Testowy
from .models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user

    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Wojtek',},
            'body': 'Pierwszy wpis od Wojtka'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

@app.route('/test', methods=['GET', 'POST'])
def testowy():
    form = Testowy()
    print('{} - {}'.format(form.validate_on_submit(), form.name.data))
    if form.validate_on_submit():
        flash('Name: {}'.format(form.name.data))
        return redirect('/index')
    return render_template('testowy.html', title='Testing Form', form=form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

