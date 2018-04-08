'''Set environment specific configurations'''
import os


class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    '''Configurations for development'''
    DEBUG = True


class TestingConfig(Config):
    '''Configuration for testing with a separate test db'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:kyalo2018@127.0.0.1:5432/testdb"
    DEBUG = True


class StagingConfig(Config):
    '''Configurations for staging'''
    DEBUG = True


class ProductionCOnfig(Config):
    '''Configurations for Production'''
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionCOnfig,
}