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
# Variables
# =========================
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = True if os.environ.get('DEBUG') == 'True' else False

PRE_URL = '/api/v1/'
api = Api(app)


# =========================
# Routes
# =========================


# Signup
@api.route(PRE_URL + 'signup')
class Signup(Resource):

    def post(self):
        return {'message': 'signup'}


# Login
@api.route(PRE_URL + 'login')
class Login(Resource):

    def post(self):
        return {'message': 'login'}


# Logout
@api.route(PRE_URL + 'logout')
class Logout(Resource):

    def get(self):
        return {'message': 'logout'}


if __name__ == "__main__":
    app.run()
