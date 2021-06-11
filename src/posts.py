from flask import Blueprint, url_for


post_bp = Blueprint(__name__, "posts")


@post_bp.route(url_for(''), methods=["POST"])
def create():
    pass
