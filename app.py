from random import randint
from flask import Flask, render_template, request
import json
import pymorphy2
import re


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query-example')
def query_example():
    text = request.args.get('text')
    reg = re.compile('[^а-яА-Я ]')
    return text





