from flask import Flask, request, json
from model.comment import Comment
from model.database import db
from model.image import Image
from model.tweet import Tweet
from model.user import User

__author__ = 'ty'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/moments?charset=utf8'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    # admin = User('admin', 'admin@example.com')
    # db.session.add(admin)
    # db.session.commit()
    return "This site is under development, will come soon."


def show_the_login_form():
    return "login form"


def valid_login(username, password):
    return True


def log_the_user_in(username):
    return "Welcome %s" % username


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            return 'Invalid username or password'
    else:
        return show_the_login_form()


@app.route("/user/<username>")
def show_user_profile(username):
    user = User.query.filter_by(username=username).first()

    if user:
        return user.json()
    else:
        return json.jsonify(error="No such user: %s" % username)


@app.route("/user/<username>/tweets")
def show_user_tweets(username):

    return "%s tweets" % username


@app.route("/user/<username>/friends")
def show_user_friends(username):
    return "%s friends" % username


@app.route("/search/<keyword>")
def show_search_result(keyword):
    return "Search result: %s" % keyword


if __name__ == "__main__":
    app.run(debug=True)
