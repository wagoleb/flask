import os

from config import basedir, Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_openid import OpenID

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import models, views

