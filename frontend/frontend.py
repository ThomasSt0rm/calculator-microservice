from __future__ import print_function
from flask import Flask, request, flash, render_template, url_for, redirect, session
import requests
import json

app = Flask(__name__)
plus_url = "http://plus:5051/api/sum"
minus_url = "http://minus:5052/api/deduct"
multi_url = "http://multi:5053/api/multi"
div_url = "http://div:5054/api/div"


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        session['first'] = request.form['first']
        session['second'] = request.form['second']
        session['action'] = request.form['action']
        numbers = { "first": session['first'], "second": session['second'] }
        if session['action'] == "Sum":
            r = requests.post(plus_url, json = numbers)
            result = json.loads(r.text)
            flash("Sum is %s" % result['result'])
            return redirect(url_for('index'))
        if session['action'] == "Deduct":
            r = requests.post(minus_url, json = numbers)
            result = json.loads(r.text)
            flash("Deduct is %s" % result['result'])
            return redirect(url_for('index'))
        if session['action'] == "Multiply":
            r = requests.post(multi_url, json = numbers)
            result = json.loads(r.text)
            flash("Multiply is %s" % result['result'])
            return redirect(url_for('index'))
        if session['action'] == "Divide":
            r = requests.post(div_url, json = numbers)
            result = json.loads(r.text)
            flash("Division is %s" % result['result'])
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'verysecuresecret'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5055)