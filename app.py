import sqlite3
import numpy as np
from flask import Flask, render_template, g, request

app = Flask(__name__)

sql_command_create_table = """
CREATE TABLE entries (
    id INTEGER PRIMARY KEY autoincrement,
    content TEXT not null
    );
"""

def init_db():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute(sql_command_create_table)
    connection.commit()
    connection.close()


def add_data(item):
    connect = sqlite3.connect('todo.db')
    print('database opened')
    connect.execute("INSERT INTO entries (content) VALUES ('{}');".format(item))
    connect.commit()
    print ('Records Created')
    connect.close()

def get_all_data():
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    print('database opened')
    cursor.execute("SELECT * FROM entries")
    todo_list = list(cursor.fetchall())
    todo_array = np.asarray(todo_list)
    return todo_array

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inputValue = request.form['todoInputName']
        add_data(inputValue)
        data = get_all_data()
        return render_template('index.html', lastInput=inputValue, todos=data)
    elif request.method == 'GET':
        data = get_all_data()
        return render_template('index.html', todos=zip(data))



if __name__ == '__main__':
    app.debug = True
    app.run()
