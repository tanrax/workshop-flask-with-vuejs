# -*- coding: utf-8 -*-
# =========================
# Librarys
# =========================
import os
from os.path import join, dirname
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from faker import Factory
from random import randint

dotenv_path = join(dirname(__file__), 'env')
load_dotenv(dotenv_path)


app = Flask(__name__)

# =========================
# Settings
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =========================
# Variables
# =========================
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

# =========================
# Help commands
# =========================


@manager.command
def fake_data():
    # Spanish
    fake = Factory.create('es_ES')

    # Reload tables
    db.drop_all()
    db.create_all()

    # Make 100 fake users
    for num in range(100):
        profile = fake.simple_profile()
        username = profile['username']
        mail = profile['mail']
        password = generate_password_hash('123')
        # Save in database
        my_user = User(username=username, mail=mail, password=password)
        db.session.add(my_user)

    print('Users created')

    # Make 1000 fake news
    for num in range(1000):
        title = fake.sentence()
        url = fake.uri()
        user_id = randint(1, 100)
        # Save in database
        my_notice = Notice(title=title, url=url, user_id=user_id)
        db.session.add(my_notice)

    print('News created')

    # Make 10000 fake comments
    for num in range(10000):
        text = fake.text()
        notice_id = randint(1, 1000)
        user_id = randint(1, 100)
        # Save in database
        my_comment = Comment(text=text, notice_id=notice_id, user_id=user_id)
        db.session.add(my_comment)

    print('Comments created')

    db.session.commit()


if __name__ == "__main__":
    manager.run()
