# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from models import User
from flask_marshmallow import Marshmallow

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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

PRE_URL = '/api/v1/'
ma = Marshmallow(app)
api = Api(app)
db = SQLAlchemy(app)
db.init_app(app)


# =========================
# Schemas
# =========================


# User
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'mail')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
        all_users = User.query.all()
        return users_schema.jsonify(all_users)


@api.route(PRE_URL + 'user/<int:id>')
class UserSingle(Resource):

    def get(self, id):
        my_user = User.query.get(id)
        if my_user:
            return user_schema.jsonify(my_user)
        else:
            return {'message': 'No existe el usuario'}, 400


if __name__ == "__main__":
    app.run()
