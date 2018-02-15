# -*- coding: utf-8 -*-

# =========================
# Librarys
# =========================
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from models import User, Notice, Comment
from flask_marshmallow import Marshmallow
from flask_cors import CORS

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
CORS(app)
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


# Notice
class NoticeSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'url', 'user_id', '_links')

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

# Notice


@api.route(PRE_URL + 'notice')
class NoticeList(Resource):

    def get(self):
        my_news = Notice.query.all()
        return news_schema.jsonify(my_news)

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Datos inválidos'}, 400
        # Validations
        try:
            title = json_data['title']
            url = json_data['url']
            user_id = json_data['user_id']
        except Exception as e:
            return {'message': 'No existen los campos necesarios'}, 400
        # Save data
        my_notice = Notice(title=title, url=url, user_id=user_id)
        db.session.add(my_notice)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'No se ha podido guardar la información'}, 500
        return {'message': 'ok'}, 200


@api.route(PRE_URL + 'notice/<int:id>')
class NewsSingle(Resource):

    def get(self, id):
        my_notice = Notice.query.get(id)
        return notice_schema.jsonify(my_notice)

    def patch(self, id):
        my_notice = Notice.query.get(id)
        if not my_notice:
            return {'message': 'No existe la noticia'}, 400
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Datos inválidos'}, 400
        # Validations
        try:
            title = json_data['title']
            url = json_data['url']
            user_id = json_data['user_id']
        except Exception as e:
            return {'message': 'No existen los campos necesarios'}, 400
        # Update data
        my_notice.title = title
        my_notice.url = url
        my_notice.user_id = user_id
        db.session.add(my_notice)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'No se ha podido guardar la información'}, 500
        return {'message': 'ok'}, 200

    def delete(self, id):
        my_notice = Notice.query.get(id)
        if my_notice:
            db.session.delete(my_notice)
            db.session.commit()
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {
                    'message': 'No se ha podido guardar la información'}, 500
        else:
            return {'message': 'No existe la noticia'}, 400
        return {'message': 'ok'}, 200


# Comment
@api.route(PRE_URL + 'notice/<int:id>/comments')
class Comments(Resource):

    def get(self, id):
        my_comments = Comment.query.filter_by(notice_id=id).all()
        return comments_schema.jsonify(my_comments)

    def post(self, id):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run()
