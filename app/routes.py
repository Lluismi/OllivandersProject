from flask import Flask, render_template
from . import app
from main import stock
from PIL import Image, ImageFilter

@app.route('/')
@app.route('/frontend/index.html')
def frontend():
    return render_template('frontend/index.html') 

@app.route('/frontend/agedBrie.html')
def AgedBrie():
    return render_template('frontend/agedBrie.html') 

@app.route('/frontend/backStagePass.html')
def BackStagePass():
    return render_template('frontend/backstagepass.html') 

@app.route('/frontend/conjured.html')
def Conjured():
    return render_template('frontend/conjured.html') 

@app.route('/frontend/normalitem.html')
def NormalItem():
    return render_template('frontend/normalitem.html')

@app.route('/frontend/sulfuras.html')
def Sulfuras():
    return render_template('frontend/sulfuras.html')

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
