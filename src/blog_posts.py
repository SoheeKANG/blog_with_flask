import flask
import json
from flask import Blueprint, url_for
from decorators import login_required


post_bp = Blueprint(__name__, "posts")


@post_bp.route(url_for('create'), methods=["POST"])
@login_required
def create():
    request = flask.request.get_data().decode()
    try:
        request = json.loads(request)
    except json.JSONDecodeError:
        return "Request is badly encoded", 400

    if any([prop not in request for prop in ["title", "content"]]):
        return "Not all request properties were specified", 400

    if len(request["title"]) == "" or len(request["content"]) == "":
        return "Request is empty", 400
    if len(request["title"]) > 100 or len(request["content"]) > 40960:
        return "Request length too long", 413

    try:
        uuid = ''
        return uuid, 200
    except Exception:
        return "Server failed to create the post. Please retry again later", 500


# @post_bp.route(url_for("get_post"))
# @post_bp.route(url_for(<int: ...>
def get_post():
    uuid = flask.request.args.get("uuid")
    if uuid is None:
        return "Bad request", 400

    post = ""
    if post is None or post == 0:
        return "Post not found", 404

    _date = ""
