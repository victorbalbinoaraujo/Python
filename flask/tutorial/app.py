# Setup
#   export FLASK_APP=app.py
#   flask run

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple 'Hello, World!'
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

# Simple math
@app.route('/simple-math', methods=['GET'])
def simple_math():
    return str(1 + 1)

# Returning JSONs
@app.route('/json', methods=['GET'])
def json_example():
    json_ex = {
        'Name'   : 'John Doe',
        'Age'    : 30,
        'Phones' : [
            {
                'Phone name'   : 'Samsung',
                'Phone number' : 12346578
            },
            {
                'Phone name'   : 'Motorola',
                'Phone number' : 87654321
            }
        ]
    }

    return jsonify(json_ex)

# POST Method
@app.route('/sum-two-numbers', methods=['POST'])
def sum_two_numbers():
    # Get x, y from posted data
    data_numbers = request.get_json()

    # Handle error
    if "x" not in data_numbers:
        return "ERROR", 305

    # Sum the two numbers
    z = data_numbers["x"] + data_numbers["y"]

    return jsonify({"Sum" : z}), 200

if __name__ == '__main__':
    app.run(debug=True)
