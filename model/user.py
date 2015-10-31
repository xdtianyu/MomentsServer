from flask import json

from model.database import db

__author__ = 'ty'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    nick = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    profile_image = db.Column(db.String(128))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
