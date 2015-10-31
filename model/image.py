from flask import json
from model.database import db

__author__ = 'ty'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<Image %r>' % self.url

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
