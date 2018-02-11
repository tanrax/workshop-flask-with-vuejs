from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello():
    return 'Hola Python Valencia!'


@app.route("/adios")
def bye():
    return 'Me voy que tengo prisa.'


if __name__ == "__main__":
    app.run()
