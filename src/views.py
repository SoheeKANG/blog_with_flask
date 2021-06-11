from flask import Blueprint


home_bp = Blueprint('home', __name__, url_prefix='/')


@home_bp.route('/')
def home():
    return "Home"


@home_bp.route('/test')
def test():
    return 'test_page'



