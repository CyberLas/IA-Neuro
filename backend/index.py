from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result')
def hello_world1():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
