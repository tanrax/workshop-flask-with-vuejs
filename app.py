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


# User
@api.route(PRE_URL + 'user')
class UserList(Resource):

    def get(self):
        return 'user list GET'


@api.route(PRE_URL + 'user/<int:id>')
class UserSingle(Resource):

    def get(self, id):
        return 'user single GET'


# Notice
@api.route(PRE_URL + 'notice')
class NoticeList(Resource):

    def get(self):
        return 'Notice list GET'

    def post(self):
        return 'Notice list POST'


@api.route(PRE_URL + 'notice/<int:id>')
class NewsSingle(Resource):

    def get(self, id):
        return 'Notice single GET'

    def patch(self, id):
        return 'Notice single PATCH'

    def delete(self, id):
        return 'Notice single DELETE'


# Comment
@api.route(PRE_URL + 'notice/<int:id>/comments')
class Comments(Resource):

    def get(self, id):
        return 'Comments GET'

    def post(self, id):
        return 'Comments POST'


# =========================
# Run
# =========================
if __name__ == "__main__":
    app.run()
