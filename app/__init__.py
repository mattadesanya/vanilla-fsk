import os
from app.app import create_app
app = create_app(os.environ.get('PY_ENV') or 'default')
