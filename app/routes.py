from flask import Flask, render_template
from . import app
from main import stock

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

@app.route('/get_items')
def get_items():
    return '<p>{}</p>'.format(stock.get_items())

@app.route('/update_quality')
def update_quallty():
    stock.update_quality(0)
    return '<p>{}</p>'.format(stock.get_items())
