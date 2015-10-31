__author__ = 'ty'

from flask import Flask

app = Flask(__name__)


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
