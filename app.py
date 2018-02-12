# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask

# =========================
# Extensions initialization
# =========================
dotenv_path = join(dirname(__file__), 'env')
load_dotenv(dotenv_path)
app = Flask(__name__)

# =========================
# Extensions initialization
# =========================
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = True if os.environ.get('DEBUG') == 'True' else False

# Alternativa
# https://github.com/direnv/direnv

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hola Python Valencia!'


if __name__ == "__main__":
    app.run()
