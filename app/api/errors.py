import traceback
import logging
from sqlalchemy.orm.exc import NoResultFound
from app.api import api

log = logging.getLogger(__name__)


@api.app_errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'},
    404
