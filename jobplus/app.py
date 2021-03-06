from flask import Flask
from .config import configs
from flask_sqlalchemy import SQLAlchemy
from jobplus.models import db


def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from jobplus.handlers import admin
    from jobplus.handlers import front
    app.register_blueprint(admin)
    app.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))


    register_extensions(app)
    register_blueprints(app)

    return app
