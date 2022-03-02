from unicodedata import name
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def cookie():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    name = request.form['nm']
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', name)
   
    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'
