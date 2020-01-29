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
    
@app.route('/backend/modificar.html')
def modificar_objeto():
    return render_template('backend/modificar.html')

@app.route('/backend/insertar.html')
def insertar_objeto():
    return render_template('backend/insertar.html')

@app.route('/get_items')
def get_items():
    return '<p>{}</p>'.format(stock.get_items())

@app.route('/update_quality')
def update_quallty():
    stock.update_quality(0)
    return '<p>{}</p>'.format(stock.get_items())
