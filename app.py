import sqlite3
from flask import Flask, render_template, g, request

app = Flask(__name__)

def connect_db(data):
    connect = sqlite3.connect('todo.db')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test = request.form['todoInputName']
        return render_template('index.html', test=test)
    return render_template('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
