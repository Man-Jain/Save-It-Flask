import os

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGOALCHEMY_DATABASE = os.environ.get('MONGOALCHEMY_DATABASE')
    MONGOALCHEMY_SERVER = os.environ.get('MONGOALCHEMY_SERVER')
    MONGOALCHEMY_PORT = os.environ.get('MONGOALCHEMY_PORT')
    MONGOALCHEMY_USER = os.environ.get('MONGOALCHEMY_USER')
    MONGOALCHEMY_PASSWORD = os.environ.get('MONGOALCHEMY_PASSWORD')
    MONGOALCHEMY_SERVER_AUTH = False
    DEBUG = False
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGOALCHEMY_DATABASE = os.environ.get('MONGOALCHEMY_DATABASE')
    MONGOALCHEMY_SERVER = os.environ.get('MONGOALCHEMY_SERVER')
    MONGOALCHEMY_PORT = os.environ.get('MONGOALCHEMY_PORT')
    MONGOALCHEMY_USER = os.environ.get('MONGOALCHEMY_USER')
    MONGOALCHEMY_PASSWORD = os.environ.get('MONGOALCHEMY_PASSWORD')
    MONGOALCHEMY_SERVER_AUTH = False
    DEBUG = False
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}