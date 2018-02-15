import pytz

from app import app, db
from datetime import datetime
from flask import render_template, flash, redirect, session, url_for, request, g, url_for
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, Testowy, Login, RegistrationForm, EditProfileForm
from models import User, Post
from tzlocal import get_localzone
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data, str(form.remember_me.data)))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])


@app.route('/test', methods=['GET', 'POST'])
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('log'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('log.html', title='Standard login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user, remember=False)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).all()
    if user.last_seen:
        time = datetime.strftime(user.last_seen, "%Y-%m-%d %H:%M:%S")
        local_timezone = get_localzone()
        utc_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        local_time = datetime.strftime(utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone), "%Y-%m-%d %H:%M:%S")
    return render_template('user.html', user=user, posts=posts, time=local_time)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)