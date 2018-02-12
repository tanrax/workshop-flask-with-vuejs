# -*- coding: utf-8 -*-
# Librarys
import os
from os.path import join, dirname
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

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


class User(db.Model):
    '''
    Table user
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    mail = db.Column(db.String(200))
    password = db.Column(db.String(106))

    def __repr__(self):
        return '<User Table {0}>'.format(self.username)
