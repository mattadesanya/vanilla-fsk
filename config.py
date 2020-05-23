"""App Configuration

Config is the base class which other classes inherit
for the different environments:
Test, Development and Production
"""

import os
import random
import string

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_DIR = "app"
    SECRET_KEY = os.getenv('SECRET_KEY') or \
        "".join(random.choice(string.ascii_uppercase + string.digits)
                for x in range(32))


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URL') \
        or "postgres://postgres@localhost:5432/fsk_test_db"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URL') \
        or "postgres://postgres@localhost:5432/fsk_dev_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
