from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data):
    if posted_data.keys() == {'op', 'x', 'y'}:
        if posted_data['y'] == 0 and posted_data['op'] == 4:
            return 302
        return 200
    return 301


def operations(op, x, y):
    return {
        1: lambda: x + y,
        2: lambda: x - y,
        3: lambda: x * y,
        4: lambda: x / y,
    }.get(op, lambda: "Opção inválida")()


class Calculate(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data)

        if status_code == 200:
            message = operations(posted_data['op'],
                                 posted_data['x'],
                                 posted_data['y']),
        elif status_code == 302:
            message = "Can't divide by 0."

        else:
            message = 'Error. Missing parameters.'

        return jsonify({'Message': message,
                        'Status Code': status_code})


api.add_resource(Calculate, '/calc')

if __name__ == '__main__':
    app.run(debug=True)
