from model.comment import dump_comments

from model.database import db
from model.user import dump_sender

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

    def serialized(self):
        tweet = {"sender": dump_sender(self.sender)}
        if self.content:
            tweet["content"] = self.content
        if self.comments:
            tweet["comments"] = dump_comments(self.comments)
        if self.images:
            tweet["images"] = self.images

        return tweet
