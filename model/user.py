from flask import json

from model.database import db

__author__ = 'ty'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nick = db.Column(db.String(128))
    avatar = db.Column(db.String(256))
    profile_image = db.Column(db.String(256))
    friends = db.Column(db.Text)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def json(self):
        user = {
            'username': self.username,
            'nick': self.nick,
            'avatar': self.avatar,
            'profile-image': self.profile_image
        }
        return json.jsonify(user)

    def sender(self):
        user = {
            'username': self.username,
            'nick': self.nick,
            'avatar': self.avatar
        }
        return json.jsonify(user)

    def serialized(self):
        return {
            'username': self.username,
            'nick': self.nick,
            'avatar': self.avatar
        }

    def serialized_friends(self):
        return dump_friends(self.friends)


def dump_sender(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user.serialized()


def dump_friends(friends_string):
    friends_ids = friends_string.split(',')
    friends = []
    for friend_id in friends_ids:
        friend = User.query.filter_by(id=friend_id).first()
        if friend:
            friends.append(friend.serialized())
    return friends
