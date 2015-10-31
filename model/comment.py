from flask import json
from model.database import db
from model.user import dump_sender

__author__ = 'ty'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __repr__(self):
        return '<Comment %r>' % self.content

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)

    def serialized(self):
        comment = {"sender": dump_sender(self.sender)}
        if self.content:
            comment["content"] = self.content

        return comment


def dump_comments(comment_string):
    comment_ids = comment_string.split(',')
    comments = []
    for comment_id in comment_ids:
        comment = Comment.query.filter_by(id=comment_id).first()
        if comment:
            comments.append(comment.serialized())

    return comments
