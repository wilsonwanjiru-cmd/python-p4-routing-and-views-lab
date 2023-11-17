#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for n in range(parameter):
        result = result + f'{n}\n'
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    result = ''
    if operation == '+':
       result = num1 + num2
    elif operation == '-':
       result = num1 - num2
    elif operation == '*':
       result = num1 * num2
    elif operation == 'div':
       result = num1 / num2
    elif operation == '%':
       result = num1 % num2
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)