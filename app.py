from flask import Flask, render_template, request

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form-example', methods=['GET'])
def form_example():
    return "ldjgldgjd"