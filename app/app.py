from flask import Flask
from app.route.route import api

import config.envion


def register_app(app: Flask):
    api.init_app(app)


def create_app() -> Flask:
    app = Flask(__name__)
    register_app(app)

    return app
