from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

    # Posts class

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), unique=False)
    quote = db.Column(db.String(200), unique=False)

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class PostSchema(ma.Schema):
    class Meta:
        fields = ('author', 'quote')

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

    # Endpoint to create new post
@app.route('/post', methods=["POST"])
def add_post():
    author = request.json['author']
    quote = request.json['quote']

    new_post = Post(author, quote)

    db.session.add(new_post)
    db.session.commit()

    post = Post.query.get(new_post.id)

    return post_schema.jsonify(post)

    # Endpoint to query all guides
@app.route("/posts", methods=["GET"])
def get_posts():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    return jsonify(result)

    # Endpoint for querying a single guide
@app.route("/post/<id>", methods=["GET"])
def get_post(id):
    post = Post.query.get(id)
    return post_schema.jsonify(post)

    # Endpoint for updating a guide
@app.route("/post/<id>", methods=["PUT"])
def post_update(id):
    post = Post.query.get(id)
    author = request.json['author']
    quote = request.json['quote']

    post.author = author
    post.quote = quote

    db.session.commit()
    return post_schema.jsonify(post)

    # Endpoint for deleting a record
@app.route("/post/<id>", methods=["DELETE"])
def post_delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return post_schema.jsonify(post)
    
    

    