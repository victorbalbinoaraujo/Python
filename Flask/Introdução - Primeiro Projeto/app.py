from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return 'Olá, mundo!'

@app.route('/magic')
def magic():
    return '<H1>Mágica!</H1>'

@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome, cidade):
    return jsonify({
        'Nome' : nome,
        'Cidade' : cidade
    })

if __name__ == '__main__':
    app.run(debug=True)