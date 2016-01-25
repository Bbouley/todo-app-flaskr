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

1. Add form to html

 ```html
  <form>
      <div class="row">
        <div class="three columns">
          <label for="todoInput">Enter Item</label>
          <input class="u-full-width" type="text" placeholder="enter todo" id="todoInput">
        </div>
      </div>
    </form>
 ```

1.

