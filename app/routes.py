from flask import Flask, render_template
from . import app
from main import stock

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Tienda Ollivanders</h1>' '<p>Escriba <b>/update_quality</b> para ver la calidad de los objetos.</p>'

@app.route('/add_object')
def add_object():
    return '<h1>Se ha añadido correctamente el objeto al inventario.</h1>'

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
    stock.update_quality(1)
    return '<p>{}</p>'.format(stock.get_items())