from app import app
from flask import render_template

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
            'body': 'Pierwszy wpis od Wojteka'
        }
    ]

    return render_template("index.html", title='Home', user=user, posts=posts)