from marshmallow import fields
# from flask_marshmallow.fields import Hyperlinks
from app.serializers import serializer


class UserSerializer(serializer.Schema):
    # fields to expose
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    # Smart hyperlinking
    # _links = Hyperlinks(
    #     {"self": serializer.URLFor("users", id="<id>")}
    # )


user_serializer = UserSerializer()
users_serializer = UserSerializer(many=True)
