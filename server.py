from json import dumps

from flask import Flask, request, make_response
from werkzeug.serving import WSGIRequestHandler
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


@app.route("/tweet/post", methods=['POST'])
def tweet_post():
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['content']
        images = request.form.getlist('images[]')
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                tweet = Tweet(user.id, content)
                image_ids = []
                if images:
                    for img in images:
                        image = Image(img)
                        db.session.add(image)
                        db.session.flush()
                        image_ids.append(image.id)
                tweet.images = ','.join(map(str, image_ids))
                db.session.add(tweet)
                db.session.commit()
                return jsonify(message="200 OK")
            else:
                return jsonify(error="No such user: %s" % username)
        else:
            return jsonify(error="Error param")


@app.route("/comment/post", methods=['POST'])
def comment_post():
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['content']
        tweet_id = request.form['tweet_id']
        if username:
            user = User.query.filter_by(username=username).first()
            tweet = Tweet.query.filter_by(id=tweet_id).first()
            if user and tweet:
                comment = Comment(user.id, content)
                db.session.add(comment)
                db.session.flush()
                tweet.add_comment(comment.id)
                db.session.commit()
                return jsonify(message="200 OK")
            else:
                return jsonify(error="No such user: %s or no such tweet" % username)
        else:
            return jsonify(error="Error param")


@app.route("/profile/update", methods=['POST'])
def profile_update():
    if request.method == 'POST':
        username = request.form['username']
        nick = request.form['nick']
        avatar = request.form['avatar']
        profile_image = request.form['profile_image']
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                user.nick = nick
                user.avatar = avatar
                user.profile_image = profile_image
                db.session.commit()
                return jsonify(message="200 OK")
            else:
                return jsonify(error="No such user: %s" % username)
        else:
            return jsonify(error="Error param")


@app.route("/search/<keyword>")
def show_search_result(keyword):
    return "Search result: %s" % keyword


if __name__ == "__main__":
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True, host='0.0.0.0', threaded=True)
