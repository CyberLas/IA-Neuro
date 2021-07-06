from flask import Flask,render_template
from test import open_door
app = Flask(__name__)


@app.route('/')
def hello_world():
    neuronal(keys)
    return render_template('./fronted/index.html')

@app.route('/result')
def hello_world():
    return render_template('./fronted/result.html')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
