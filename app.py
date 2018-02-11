from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True

lista_compra = {'comida': ['pitón', 'chocolate', 'mayonesa']}


@app.route("/lista")
def lista():
    return jsonify(lista_compra)


@app.route("/lista", methods=('POST',))
def lista_post():
    data = request.get_json()
    lista_compra['comida'].append(data['nueva'])
    return jsonify(lista_compra)


if __name__ == "__main__":
    app.run()
