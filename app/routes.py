from flask import Flask, render_template
from . import app

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/add_object')
def add_object():
    return '<h1>Hello World!</h1>'

@app.route('/edit_object')
def edit_object():
    return '<h1>Hi</h1>'

@app.route('/delete_object')
def delete_object():
    return '<h1>eliminado</h1>'
