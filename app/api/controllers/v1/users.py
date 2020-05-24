from app.api import api


@api.route('/')
def index():
    return 'Welcome to my API'
