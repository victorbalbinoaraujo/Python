from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    # Get x and y from posted data
    data_dict = request.get_json()

    # Handle errors
    if 'x' not in data_dict:
        return "ERROR", 305

    # Add z = x + y
    z = data_dict['x'] + data_dict['y']

    # return JSON z
    return jsonify({"Sum": z}), 200


if __name__ == '__main__':
    app.run(debug=True)
