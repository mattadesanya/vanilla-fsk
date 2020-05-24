"""Base Model

Other database models will inherit the properties of the base model
"""
from app.database import db


class Model(db.Model):
    """The Base model class"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    f_id = db.Column(db.String(50), primary_key=True)
    created_by = db.Column(db.String(50))
    updated_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
