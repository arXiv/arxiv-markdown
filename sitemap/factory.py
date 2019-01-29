"""Sitemap app factory."""

import logging

from flask import Flask
from flask_s3 import FlaskS3
from arxiv.base import Base
from . import routes

s3 = FlaskS3()


def create_web_app() -> Flask:
    """Initialize an instance of the sitemap application."""
    from . import config

    app = Flask(__name__)
    app.config.from_object(config)

    Base(app)
    s3.init_app(app)

    app.register_blueprint(routes.blueprint)     # Provides base templates.

    return app
