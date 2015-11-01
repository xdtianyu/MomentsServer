from json import dumps

from flask import Flask, request, make_response
from model.database import db
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


def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    res = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys, ensure_ascii=False))
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    res.status_code = status
    return res


def response_json(status=200, json_dumps=None):
    res = make_response(json_dumps)
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    res.status_code = status
    return res


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
        return jsonify(error="No such user: %s" % username)


@app.route("/user/<username>/tweets")
def show_user_tweets(username):
    user = User.query.filter_by(username=username).first()

    if user:

        # return dumps(user.serialized_tweets(), ensure_ascii=False)

        # return jsonify(tweets=user.serialized_tweets())
        return response_json(
            json_dumps=dumps(user.serialized_tweets(), ensure_ascii=False, sort_keys=True, indent=2,
                             separators=(',', ': ')))
    else:
        return jsonify(error="No such user: %s" % username)


@app.route("/user/<username>/friends")
def show_user_friends(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(friends=user.serialized_friends())
    else:
        return jsonify(error="No such user: %s" % username)


@app.route("/search/<keyword>")
def show_search_result(keyword):
    return "Search result: %s" % keyword


if __name__ == "__main__":
    app.run(debug=True)
