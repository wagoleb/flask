from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
db = create_engine("mysql://employees:P@$sw0rd001@localhost/employees")

from app2 import models, views
