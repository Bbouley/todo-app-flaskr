### TODO App

## Outline

- Build a basic todo app and deploy to heroku

## Things to work out

- Creating a server with python
- Running server locally
- Creating a DB connection using sql
- Build sql Schema
- Sending HTML and CSS with python
- Sending form/input information to python server
- Creating an endpoint to display page
- CRUD with python


## Documentation on my steps

1. Create dir, activate virtualenv and install flask

    ```sh
    $ pyvenv-3.5 env
    $ source env/bin/activate
    $ pip3 install Flask
    ```

1. Build project structure

    ```
    |-env (created by venv)
    |-static (for css)
    |-templates (for html)
    |-app.py
    |-readme.md
    |-.gitignore
    ```

1. Add files to be ignored into gitignore

    ```
    env
    *.pyc
    *.DS_Store
    __pycache__
    ```

1. Build hello_world in app.py

    ```py
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.debug = True
        app.run()
     ```

  - Adding in ```app.debug = True``` means the server reloads itself on code changes and provides a debugger if things go wrong

1. Add in new routes to mess around a bit

    ```py
    @app.route('/hello')
    def hello_world():
        return 'Hello World!'

    @app.route('/')
    def index():
        return 'This is the index page'
  ```

1. Add index.html to templates
1. Download skeleton and normalize.css and put into static folder, add links to html page. Build html page with test to check user templates

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flaskr TODO</title>
        <link rel="stylesheet" href="{{url_for('static', filename='normalize.css')}}">
        <link rel="stylesheet" href="{{url_for('static', filename='skeleton.css')}}">
        <link rel="stylesheet" href="{{url_for('static', filename='styles.css')}}">
    </head>
    <body>

        <h1>To Do</h1>

        <h2>Testing section</h2>

        {% if name %}
            <h2>Hello {{ name }}</h2>
        {% else %}
            <h2>Hello World!!</h2>
        {% endif %}

    </body>
    </html>
    ```
1. add ```render_template``` to import, and build new route to render index

    ```py
    from flask import Flask, render_template
    ```

    ```py
    @app.route('/')
    def index(name=None):
        return render_template('index.html', name=name)
    ```

1. Add form to html, include action as shown below

    ```html
    <form action="{{ url_for('index') }}" method="post" class="add-entry">
      <div class="row">
        <div class="three columns">
          <label for="todoInput">Enter Item</label>
          <input class="u-full-width" type="text" placeholder="enter todo" id="todoInput" name="todoInputName">
        </div>
      </div>
    </form>
    ```

1. add sql schema

      ```
      drop table if exists entries;
      create table entries (
        id integer primary key autoincrement
        content text not null
      );
      ```

1. edit route to allow post requests to / endpoint. Also changed to pull form value off and calls add_data function with input value.

    ```py
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            test = request.form['todoInputName']
            return render_template('index.html', test=test)
        return render_template('index.html')
    ```
    - This is saying if it is a post request, pull of the information from form value input called 'todoInputName'. Then render index.html with this passed in. NOTE - Index.html testing section has been changed.

    ```html
    {% if test %}
      <h2>Hello {{ test }}</h2>
    {% else %}
      <h2>Hello World!!</h2>
    {% endif %}
    ```

1. add ```import sqlite3```
1. create db config in app.py
1. add ```g``` to import from flask
1. create connect_db function, which will take a variable. open up connnection to db. Add arguments to database. close connection

    ```py
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
    ```

1. added read function to get data from database, and edited index route to get data. also added get data function to get route. sending todos object back to server, but ids are also being sent currently. html changed to reflect and display this.

    ```py
    def get_all_data():
        connect = sqlite3.connect('todo.db')
        cursor = connect.cursor()
        print('database opened')
        cursor.execute("SELECT * FROM entries ORDER BY id desc")
        return list(cursor.fetchall())
    ```

    ```py
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputValue = request.form['todoInputName']
            add_data(inputValue)
            return render_template('index.html', lastInput=inputValue)
        elif request.method == 'GET':
            data = get_all_data()
            print(data)
            return render_template('index.html', todos=data)
    ```

    ```html
    <div class="list">
      <ul>
      {% for todo in todos %}
        <li>{{ todo[1] }}</li>
      {% endfor %}
      </ul>
    </div>
    ```

1. Add id to li element being created using todo[0], and add a delete button to those as well.

    ```html
    <div class="list">
      <ul>
      {% for todo in todos %}
        <li id = {{ todo[0] }}>
          <h3>{{ todo[1] }}</h3>
          <button class="delete">X</button>
        </li>
      {% endfor %}
      </ul>
    </div>
    ```

1. Create a main.js file in static folder and then add in scripts for both jquery and the main.js file at the bottom of the html

    ```html
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
    <script type="text/javascript" src="../static/main.js"></script>
    ```

1. Create an ajax request on button click so when user clicks the x button it will send ajax query GET request to server side. Note the format of the on click function. This is because we are created our li elements dynamically so we have to use delegated events.

    ```js
    $(document).on('ready', function() {

        $(document).on('click', '.delete', function(e) {
            var $db_id = $(this).parent().attr('id')
            var $this = $(this)
            $.ajax({
                url: '/delete/' + $db_id,
                method: 'GET',
                success: function(result) {
                //Code Things Here
                }
            });
        });
    });
    ```

1. Add in route on server that corresponds to the route the ajax request will hit. Then use try/except to either return error or success object depending on the db connection result. We also have to add in jsonify to import from flask, so we can send json objects back

    ```py
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
    ```

1. So we now have a setup that will hit the database and return error object if deletion is unsuccessful or success object if successful. We send this object back to client and can perform logic on it with jquery. So now the whole ajax call with logic, looks like this:

    ```js
    $(document).on('click', '.delete', function(e) {
        var $db_id = $(this).parent().attr('id')
        var $this = $(this)
        $.ajax({
            url: '/delete/' + $db_id,
            method: 'GET',
            success: function(result) {
                if(result.status === 1) {
                    $this.parent().remove()
                }
            }
        });
    });
    ```

1. Starting edit route. Add an edit button to html, then target it with jquery and append an edit box with a new button that can be used to send information to the server with an ajax request. Below is the code to add button to html with class sendEdit, which I can then later add another event listener to to send information to server.

    ```html
    <div id = {{ todo[0] }}>
        <h3>{{ todo[1] }}</h3>
        <button class="delete">X</button>
        <button class="edit">Edit</button>
    </div>
    ```

    ```js
    $(document).on('click', '.edit', function() {
        var thisEl = thisEl
        var $db_id = thisEl.parent().attr('id')
        var element = '<input type="text" id="' + $db_id + '" required></input>'
        var buttonElement = '&lt;<button class="sendEdit">Edit</button>'
        thisEl.parent().append(element);
        thisEl.parent().append(buttonElement);
        thisEl.hide()
    });
    ```

1. Next step is adding an event listener to .sendEdit. On click I want it to grab the form value of the dynamically created form and send that as an edit to my server. At the moment, when information is sent back, I want the page to reload. There needs to be a change here, so that I can handle any errors in editing something in the database.

    ```js
    $(document).on('click', '.sendEdit', function() {
        var thisEl = $(this)
        var edit = {
            data: thisEl.prev().val()
        }
        var $db_id = thisEl.parent().attr('id')
        $.ajax({
            url: '/edit/' + $db_id,
            contentType: 'application/json',
            method: 'POST',
            data: JSON.stringify(edit),
            datatype: 'json',
            success: function(result) {
                window.location.reload();
            }
        });
    });
    ```

1. Now I needed to set up a route that would handle the incoming request and make the appropriate call to the database updating entry, and handling any errors if there were any. Finally, sending the appropriate object back to the client-side. In order to get the POST request as json, I had to call get_json on the request, and then use bracket notation (NOT DOT), to get the form value I was looking for. Which comes in as {data : 'some value'}.

    ```py
    @app.route('/edit/<todo_id>', methods=['POST'])
    def edit_entry(todo_id):
        result = {'status' : 0, 'message' : 'Error'}
        data_object = request.get_json()
        update = data_object['data']
        print (update)
        try:
            connect = sqlite3.connect('todo.db')
            connect.execute("UPDATE entries SET content = ? WHERE ID = ?;", (update, todo_id,))
            connect.commit()
            connect.close()
            result = {'status': 1, 'message' : 'TODO Edited'}
        except:
            result = {'status': 0, 'message' : 'Error'}
        return jsonify(result)
    ```


## Questions/Issues



