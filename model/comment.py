from flask import json
import time
from model.database import db
from model.user import dump_sender

__author__ = 'ty'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)
    time_post = db.Column(db.Integer)
    time_update = db.Column(db.Integer)

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.time_post = int(time.time())
        self.time_update = self.time_post

    def __repr__(self):
        return '<Comment %r>' % self.content

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)

    def serialized(self):
        comment = {
            "id": self.id,
            "sender": dump_sender(self.sender)
        }
        if self.content:
            comment["content"] = self.content

        return comment


def dump_comments(comment_string):
    comments = []
    if comment_string:
        comment_ids = comment_string.split(',')
        comments = Comment.query.filter(Comment.id.in_(comment_ids)).order_by(Comment.time_post.desc()).all()

    return [comment.serialized() for comment in comments]
