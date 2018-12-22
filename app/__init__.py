from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from config import app_config
from flask_bootstrap import Bootstrap

db = MongoAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    '''app.config.from_pyfile('config.py')'''
    db.init_app(app)
    Bootstrap(app)

    from app import models

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix = '/api')

    return app