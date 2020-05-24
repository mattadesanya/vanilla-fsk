# pylint: disable=unused-argument
"""App Test

This test is simply to check if the test suite is successfully
calling the factory create_app function
"""

from flask import current_app


def test_app_exists(app):
    """Check if there is a current app"""
    assert current_app is not None


def test_app_is_testing(app):
    """Check if current app config is Test"""
    assert current_app.config['TESTING']
