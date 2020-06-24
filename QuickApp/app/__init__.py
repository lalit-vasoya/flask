from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page!'

@app.route('/hello')
def hello():
    return 'Hello Page!'

@app.route('/user/<username>')
def user_page(username):
    return "Hello "+username

@app.route('/user/<int:id>')
def user_id(id):
    return "user "+str(id)

@app.route('/user/<float:id>')
def user_float(id):
    return "Hello 2 "+str(id)

@app.route('/user/<path:path>')
def user_path(path):
    return "Path "+escape(path)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST METHOD'
    else:
        return 'GET METHOD<form method="post"><button type="submit">POST</button></form>'


@app.route('/render')
@app.route('/render/<name>')
def render(name=None):
    return render_template('index.html',name=name)

with app.test_request_context():
    print( url_for('index') )
    print( url_for('hello',next="/") )