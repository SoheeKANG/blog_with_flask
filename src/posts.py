import os
import sys
import json
from flask import Blueprint, current_app, url_for, request


post_bp = Blueprint(__name__, "posts")


@post_bp.route(url_for(''), methods=["POST"])
def create():
    pass
