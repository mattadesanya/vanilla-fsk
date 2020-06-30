"""Main Flask Application

The main flask application starts here
by calling the create_app factory function

Parameter: os.environ.get('PY_ENV')
This is the environment that is mirrored in the config file.
If PY_ENV is not set, then default is used.
"""

import os
import app.controllers.api.v1  # noqa: F401
import app.controllers.auth.auth_controller  # noqa: F401
import app.models.permission  # noqa: F401
from app.app import create_app
flask_app = create_app(os.environ.get('PY_ENV') or 'default')
