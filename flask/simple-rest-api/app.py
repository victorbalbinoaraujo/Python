from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data):
    if posted_data.keys() == {'x', 'y'}:
        return 200
    return 301

class Add(Resource):
    def post(self):
        posted_data = request.get_json()
        status_code = check_posted_data(posted_data)
        message = {
            200 : sum(posted_data.values()),
            301 : 'Error'
        }
        return jsonify({'Message' : message[status_code],
                        'Status Code' : status_code})

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


api.add_resource(Add, '/add')
# @app.route('/')

if __name__ == '__main__':
    app.run(debug=True)
