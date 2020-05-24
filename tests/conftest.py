"""Global Fixture

This helps to share fixture accross different tests setup
"""

import pytest
from app.app import create_app
# from app.database import db


@pytest.fixture(scope="session")
def app():
    """Call create_app factory with test parameter"""
    test_app = create_app('testing')
    app_context = test_app.app_context()
    app_context.push()

    def tear_down():    # pylint: disable=unused-variable
        # db.session_remove()
        # db.drop_all()
        app_context.pop()

    return test_app


# pylint: disable=redefined-outer-name
@pytest.fixture(scope="function")
def client(app):
    """Create client fixture at the function level"""
    return app.test_client()
