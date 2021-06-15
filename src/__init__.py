from flask import Flask, render_template
import config


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile(config)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
