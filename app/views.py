from app import app, db
from flask import render_template, flash, redirect, session, url_for, request, g, url_for
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, Testowy, Login
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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

@app.route('/test', methods=['GET', 'POST'])
def testowy():
    form = Testowy()
    if form.validate_on_submit():
        flash('Name: {}'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('testowy.html', title='Testing Form', form=form)

@app.route('/parametr/<name>')
def param(name):
    return render_template('param.html', title='Przekazanie prametru', param=name)

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = Login()
    if form.validate_on_submit():
        flash('Username: {}, Password: {}, Remember Me: {}'.format(form.username.data, form.password.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('log.html', title='Standard login', form=form)
