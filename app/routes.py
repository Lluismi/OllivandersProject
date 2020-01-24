from flask import Flask, render_template
from . import app
from main import stock

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/frontend/index.html')
def frontend():
    return render_template('frontend/index.html')

@app.route('/backend/index.html')
def backend():
    return render_template('backend/index.html')
    
@app.route('/edit_object')
def edit_object():
    return '<h1>Se ha modificado los datos del objeto correctamente.</h1>'

@app.route('/delete_object')
def delete_object():
    return '<h1>Se ha eliminado el objeto correctamente.</h1>'

@app.route('/get_items')
def get_items():
    return '<p>{}</p>'.format(stock.get_items())

@app.route('/update_quality')
def update_quallty():
    stock.update_quality(0)
    return '<p>{}</p>'.format(stock.get_items())
