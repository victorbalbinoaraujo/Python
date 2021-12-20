# To RUN -> Terminal
# export FLASK_APP=app.py
# flask run

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hithere')
def hithere_everyone():
    return 'I just hit hi there (or hit here?)'


@app.route('/simple_math')
def simple_math():
    a = 34 + 6
    a_str = str(a)
    return a_str


@app.route('/json_example')
def json_example():
    json = {
        'field_1': 'abc',
        'field_2': 'def'
    }
    return jsonify(json)


@app.route('/person')
def person():
    person_json = {
        'Name': 'Victor',
        'Age': 21,
        'Emails': [
                'fakemail@fake.com',
                'emailfake@email.com'
        ],
        'Phones': [
            {
                'phone_name': 'Iphone8',
                'phone_number': 1234567890
            },
            {
                'phone_name': 'Samsung Galaxy',
                'phone_number': 1234098765
            }
        ]
    }
    return jsonify(person_json)


if __name__ == '__main__':
    app.run(debug=True)
