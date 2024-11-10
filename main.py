from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions


app = Flask(__name__)
api = Api(app)


class Post(Resource):
    def get(self, id=0):
        if not id:
            posts = db_actions.get_posts()



def row_to_json(posts: list):
    posts_json = []

    for post in posts:
        posts_json.append({
            "id": post.id,
            "author": posts.author,
            "text": post.text
        })
        posts_json = jsonify(posts_json)
        posts_json.status_code = 200

    return posts_json