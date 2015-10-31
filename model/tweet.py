from flask import json

from model.database import db

__author__ = 'ty'


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)
    images = db.Column(db.Text)
    comments = db.Column(db.Text)

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __repr__(self):
        return '<Tweet %r>' % self.content

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
