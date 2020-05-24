from app.controllers.api import api_v1 as api


@api.route('/users')
def index():
    return 'Welcome to my API'
