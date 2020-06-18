# pylint: disable=too-few-public-methods
"""App Configuration

Config is the base class which other classes inherit
for the different environments:
Test, Development and Production
"""

import os
import random
import string
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def fetch_secret_key(key_name):
    """ Get the secret key from environment
    Or dynamically generate a new one """
    return os.getenv(key_name) or \
        "".join(random.choice(string.ascii_uppercase + string.digits)
                for x in range(32))


class Config:
    """Base Config Class

    The JWT_ACCESS_TOKEN_EXPIRES field sets the time an access token
    will last. If set to False, then the access token will never expire.
    The JWT_REFRESH_TOKEN_EXPIRES field sets how long a refresh
    token will last. The default is 180 days, but if set to False, the
    refresh token will last forever.

    JWT_BLACKLIST_ENABLED = True simply mean that we are checking blacklisted
    tokens in this project, which is the default.
    We can add 'access' to the list of JWT_BLACKLIST_TOKEN_CHECKS.
    By default, we check 'refresh' tokens only
    """
    APP_DIR = "app"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=180)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['refresh']
    SECRET_KEY = fetch_secret_key('SECRET_KEY')
    JWT_SECRET_KEY = fetch_secret_key('JWT_SECRET_KEY')


class TestConfig(Config):
    """Test Configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URL') \
        or "postgres://postgres@localhost:5432/fsk_test_db"


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URL') \
        or "postgres://postgres@localhost:5432/fsk_dev_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'testing': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
