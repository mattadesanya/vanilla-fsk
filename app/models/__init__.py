"""All modelss imports

The file stores all the model imports used by the app
The line:
import app.models in app/__init__.py uses this file
"""

import app.models.blacklist_token  # noqa: F401
import app.models.client_api_key  # noqa: F401
import app.models.permission  # noqa: F401
import app.models.role_permission  # noqa: F401
import app.models.role  # noqa: F401
import app.models.user  # noqa: F401
