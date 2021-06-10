import os
import sys
import json
from flask import Blueprint, current_app


post_bp = Blueprint(__name__, "posts")

