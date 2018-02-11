from app import app

@app.route('/')
@app.route('/index')
def index():
    return 20*"hELLO world !!!"