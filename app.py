# -*- coding: utf-8 -*-
# Librarys
import os
from flask import Flask
from flask_restplus import Resource, Api
from dotenv import load_dotenv, find_dotenv
from models import db, User, News, Comment

load_dotenv(find_dotenv())


app = Flask(__name__)

# Config Flask
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Config API
api = Api(app)
PRE_URL = '/api/v1/'


@api.route(PRE_URL + 'signup')
class Signup(Resource):

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'login')
class Login(Resource):

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'login')
class Logout(Resource):

    def get(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'news')
class News_all(Resource):

    def get(self):
        my_news = News.query.all()
        return ([i.serialize for i in my_news])

    def post(self):
        return {'hello': 'world'}


@api.route(PRE_URL + 'news/<int:id>')
class News_single(Resource):

    def get(self, id):
        return {'hello': id}


@api.route(PRE_URL + 'news/<int:id>/comments')
class Comments(Resource):

    def get(self, id):
        return {'hello': 'world'}

    def post(self, id):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG') == 'True' if True else False)

