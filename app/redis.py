"""A single source of truth for the redis object"""

from flask_redis import FlaskRedis

redis_client = FlaskRedis()
