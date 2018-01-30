from __future__ import print_function
from flask import Flask, json, request, Response
import json

app = Flask(__name__)

def multi(number1, number2):
    multi = int(number1) * int(number2)
    return multi

@app.route('/')
def index():
    return "Hello, this is example microservice app Plus!"

@app.route('/api')
def api_test():
    msg = '{ status: "OK" }'
    return msg

@app.route('/api/multi', methods = ["POST"])
def api_multi():
    if request.headers["Content-Type"] == "application/json":
        input_data = json.dumps(request.json)
        data = json.loads(input_data)
        number1 = data["first"]
        number2 = data["second"]
        result_multi = multi(number1, number2)
        result = { "result": result_multi }
        js = json.dumps(result)
        resp = Response(js, status = 200, mimetype="application/json")
        return resp
    else:
        return '{ status: "failed", message: "wrong input or method"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5053)