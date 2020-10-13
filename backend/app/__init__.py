import os

import click
from flask import Flask, jsonify
import flask_excel

from app.config import app_config
from app.controllers import *
from app.extends.error import HttpError
from app.extensions import db, migrate, cors
from app.middlewares import before_request
from app.models.database import *


def create_app(config_name: str = None) -> Flask:
    """
    :param config_name: str in ['development', 'production', 'testing']
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    register_errorhandler(app)
    register_blueprints(app)
    register_extensions(app)
    register_middleware(app)

    return app


def register_errorhandler(app: Flask):
    @app.errorhandler(HttpError)
    def handle_http_error(error: HttpError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def register_blueprints(app: Flask):
    app.register_blueprint(admin_bp)


def register_extensions(app: Flask):
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    flask_excel.init_excel(app)


def register_middleware(app: Flask):
    app.before_request(before_request)
