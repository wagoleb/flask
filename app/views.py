from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Wojciech'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
    <h2> '''+ 500*'OLE\n' +'''</h2>
  </body>
</html>
'''