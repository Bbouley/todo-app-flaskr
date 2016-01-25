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

 |-env (created by venv)
 |-static (for css)
 |-templates (for html)
 |-app.py
 |-readme.md
 |-.gitignore

1. Add files to be ignored into gitignore

```
env
*.pyc
*.DS_Store
__pycache__
```

1.
