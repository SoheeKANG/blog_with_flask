from flask import Flask
import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    from .views import home_bp
    app.register_blueprint(home_bp)

    return app
