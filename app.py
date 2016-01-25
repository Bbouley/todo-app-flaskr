from flask import Flask, render_template
# from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
  return 'Hello World!'

@app.route('/')
def index(name=None):
  return render_template('index.html', name=name)

if __name__ == '__main__':
  app.debug = True
  app.run()
