from app2 import app
from app2.models import session, Employees
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    employees = session.query(Employees).filter(Employees.last_name.like('%Nan')).all()
    return render_template('index.html', employees=employees)
