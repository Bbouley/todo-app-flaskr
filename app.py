import sqlite3
# import numpy as np
from flask import Flask, render_template, g, request, jsonify

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
    connect.execute("INSERT INTO entries (content) VALUES ('{}');".format(item))
    connect.commit()
    connect.close()

def get_all_data():
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM entries ORDER BY id desc")
    todo_list = cursor.fetchall()
    return todo_list

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
        return render_template('index.html', todos=data)

@app.route('/delete/<todo_id>', methods=['GET'])
def delete_entry(todo_id):
    result = {'status' : 0, 'message' : 'Error'}
    try:
        print(todo_id)
        connect = sqlite3.connect('todo.db')
        print('DB opened')
        connect.execute("DELETE FROM entries WHERE id = ?", (todo_id,))
        connect.commit()
        connect.close()
        result = {'status': 1, 'message' : 'TODO Deleted'}
    except:
        result = {'status': 0, 'message': 'Error'}
    return jsonify(result)



if __name__ == '__main__':
    app.debug = True
    app.run()
