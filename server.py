from flask import Flask
from model.database import db
from model.tweet import Tweet
from model.user import User

__author__ = 'ty'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/moments'

db.init_app(app)

with app.app_context():
    db.create_all()
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()

    tweet = Tweet(1, "test")

    db.session.add(tweet)
    db.session.commit()


@app.route("/")
def index():
    return "This site is under development, will come soon."


@app.route("/user/<username>")
def show_user_profile(username):
    return "%s profile" % username


@app.route("/user/<username>/tweets")
def show_user_tweets(username):
    return "%s tweets" % username


if __name__ == "__main__":
    app.run()
