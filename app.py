import flask
from flask import Flask, render_template, request
import json



app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query-example', methods=['POST'])
def query_example():
    text = request.get_data(as_text=True)
    print(text)
    return json.dumps(['товар1', 'товар2', 'товар3'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


