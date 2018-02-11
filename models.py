# -*- coding: utf-8 -*-
# Librarys
import os
from os.path import join, dirname
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'env')
load_dotenv(dotenv_path)


app = Flask(__name__)

# Settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
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
    mail = db.Column(db.String(200))
    password = db.Column(db.String(106))
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User Table {0}>'.format(self.username)


class Notice(db.Model):
    '''
    Table Notice
    '''

    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(500))
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    # Relations
    user = db.relationship(
        'User',
        backref=db.backref(
            'Notice',
            lazy=True,
            cascade="all, delete-orphan"))

    def __repr__(self):
        return '<Notice Table {0}>'.format(self.title)


class Comment(db.Model):
    '''
    Table Comment
    '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    notice_id = db.Column(
        db.Integer, db.ForeignKey('news.id'), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    # Relations
    user = db.relationship(
        'User',
        backref=db.backref(
            'Comment',
            lazy=True,
            cascade="all, delete-orphan"))
    notice = db.relationship('Notice', backref=db.backref(
        'Comment', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return '<Comment Table {0}>'.format(self.id)


if __name__ == "__main__":
    manager.run()
