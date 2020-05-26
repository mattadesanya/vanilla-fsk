"""db Util

This class is used by all DAO objects.
"""
from app.database import db
from app.util.firebase_push_id import PushID

fancy_id = PushID()


class DbUtil(object):

    @classmethod
    def get_all(cls, model):
        return model.query.all()

    @classmethod
    def get(cls, model, id):
        return model.query.filter_by(id=id).first_or_404()

    @classmethod
    def save_to_db(cls, data):
        if not data.f_id:
            data.f_id = fancy_id.next_id()
        db.session.add(data)
        db.session.commit()
        return data.f_id
