from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'index.js'

@app.route('/result')
def hello_world():
    return 'Your are Test'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
