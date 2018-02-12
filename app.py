# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask_restplus import Resource, Api

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

api = Api(app)


# =========================
# Routes
# =========================


# User
@api.route('/user')
class User(Resource):

    def get(self):
        return {'message': 'te doy info del user'}

    def post(self):
        return {'message': 'te hago un nuevo un user'}

    def patch(self):
        return {'message': 'te actualizo un user'}

    def delete(self):
        return {'message': 'te borro un user'}


if __name__ == "__main__":
    app.run()
