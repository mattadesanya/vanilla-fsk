"""Users Controller"""

from app.controllers.api import api_v1 as api
from app.models.user import User


@api.route('/users')
def index():
    """Calls api/v1/users

    This controller returns all users
    """
    return 'Welcome to my API'
