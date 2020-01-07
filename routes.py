from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/add_object')
def add_object():
    return '<h1>Hello World!</h1>'

@app.route('/edit_object')
def edit_object():
    return Hi

@app.route('/delete_object')
def delete_object():
    return eliminado

app.run(port = 3000, debug = True)