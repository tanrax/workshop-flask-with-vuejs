# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from flask import Flask, request
from flask_restplus import Resource, Api
from dotenv import load_dotenv, find_dotenv
from models import db, User, Notice, Comment
from flask_marshmallow import Marshmallow

# =========================
# Extensions initialization
# =========================
load_dotenv(find_dotenv())
app = Flask(__name__)
ma = Marshmallow(app)
api = Api(app)

# =========================
# Configurations
# =========================
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
PRE_URL = '/api/v1/'

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


# Notice
class NoticeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'link', 'user_id', '_links')

    _links = ma.Hyperlinks({
        'comments': ma.URLFor('comments', id='<id>'),
        'user': ma.URLFor('user_single', id='<user_id>')
    })


notice_schema = NoticeSchema()
news_schema = NoticeSchema(many=True)


# Comment
class CommentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('text', '_links')

    _links = ma.Hyperlinks({
        'notice': ma.URLFor('news_single', id='<id>'),
        'user': ma.URLFor('user_single', id='<user_id>')
    })


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


# =========================
# Routes
# =========================


# Signup
@api.route(PRE_URL + 'signup')
class Signup(Resource):

    def post(self):
        return {'hello': 'world'}


# Login
@api.route(PRE_URL + 'login')
class Login(Resource):

    def post(self):
        return {'hello': 'world'}


# Logout
@api.route(PRE_URL + 'logout')
class Logout(Resource):

    def get(self):
        return {'hello': 'world'}


# User
@api.route(PRE_URL + 'user')
class UserList(Resource):

    def get(self):
        all_users = User.query.all()
        return users_schema.jsonify(all_users)


@api.route(PRE_URL + 'user/<int:id>')
class UserSingle(Resource):

    def get(self, id):
        all_users = User.query.get(id)
        return user_schema.jsonify(all_users)


# Notice
@api.route(PRE_URL + 'notice')
class NoticeList(Resource):

    def get(self):
        my_news = Notice.query.all()
        return news_schema.jsonify(my_news)

    def post(self):
        return request.form


@api.route(PRE_URL + 'notice/<int:id>')
class NewsSingle(Resource):

    def get(self, id):
        my_notice = Notice.query.get(id)
        return notice_schema.jsonify(my_notice)

    def path(self, id):
        my_notice = Notice.query.get(id)
        return notice_schema.jsonify(my_notice)

    def delete(self, id):
        my_notice = Notice.query.get(id)
        return notice_schema.jsonify(my_notice)


# Comment
@api.route(PRE_URL + 'notice/<int:id>/comments')
class Comments(Resource):

    def get(self, id):
        my_comments = Comment.query.filter_by(notice_id=id).all()
        return comments_schema.jsonify(my_comments)

    def post(self, id):
        return {'hello': 'world'}


# =========================
# Run
# =========================
if __name__ == '__main__':
    app.run(debug=True if os.environ.get('DEBUG') == 'True' else False)

