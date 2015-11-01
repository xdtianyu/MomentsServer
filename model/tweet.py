import time
from model.comment import dump_comments
from model.database import db
from model.image import dump_images
from model.user import dump_sender

__author__ = 'ty'


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text)
    images = db.Column(db.Text)
    comments = db.Column(db.Text)
    time_post = db.Column(db.Integer)
    time_update = db.Column(db.Integer)

    def __init__(self, sender, content=None, images=None):
        self.sender = sender
        self.content = content
        self.images = images
        self.time_post = int(time.time())
        self.time_update = self.time_post

    def __repr__(self):
        return '<Tweet %r>' % self.content

    def serialized(self):
        tweet = {"sender": dump_sender(self.sender)}
        if self.content:
            tweet["content"] = self.content
        if self.comments:
            tweet["comments"] = dump_comments(self.comments)
        if self.images:
            tweet["images"] = dump_images(self.images)

        return tweet


def dump_tweets(user_id, friends=None):
    users = [user_id]
    if friends:
        users.extend(friends.split(','))

    tweets = Tweet.query.filter(Tweet.sender.in_(users)).order_by(Tweet.time_post.desc()).all()
    return [tweet.serialized() for tweet in tweets]
