"""Application Error Handler"""

import traceback
import logging
from sqlalchemy.orm.exc import NoResultFound
from app.controllers.api import api    # pylint: disable=no-name-in-module

log = logging.getLogger(__name__)


@api.app_errorhandler(NoResultFound)
def database_not_found_error_handler(err):    # pylint: disable=unused-argument
    """database not found error handler
    """
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, \
        404
