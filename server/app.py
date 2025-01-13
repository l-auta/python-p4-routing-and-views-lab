#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    
    return f'{param}'

@app.route('/count/<int:param>')
def count(param):
    # Create a list of numbers from 0 to param-1
    numbers = '\n'.join(str(i) for i in range(param))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Handling division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed.", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation.", 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
