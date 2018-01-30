# -*- coding: utf-8 -*-
# Librarys
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# Settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Variables
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    '''
    Table user
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    password = db.Column(db.String(106))
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User Table {0}>'.format(self.username)


class News(db.Model):
    '''
    Table News
    '''
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(500))
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(
        'User', backref=db.backref('News', lazy=True))

    def __repr__(self):
        return '<News Table {0}>'.format(self.title)


class Comment(db.Model):
    '''
    Table Comment
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    news_id = db.Column(
        db.Integer, db.ForeignKey('news.id'), nullable=False)
    news = db.relationship(
        'News', backref=db.backref('Comment', lazy=True))

    def __repr__(self):
        return '<Comment Table {0}>'.format(self.id)


if __name__ == "__main__":
    manager.run()
