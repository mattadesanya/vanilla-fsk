"""db Util

This class is used by all DAO objects.
"""
from app.database import db
from app.util.firebase_push_id import PushID


class DbUtil:
    """
    The DBUtil class is a helper class that
    implements most of the common DB methods
    """
    @classmethod
    def get_all(cls, model):
        """ Get all records from the database """
        return model.query.all()

    @classmethod
    def get(cls, model, table_id):
        """ Return a database record by the primary key id """
        return model.query.filter_by(id=table_id).first_or_404()

    @classmethod
    def get_by_fid(cls, model, fancy_id):
        """ Return a database record by the fancy id """
        return model.query.filter_by(f_id=fancy_id).first_or_404()

    # pylint: disable=no-member
    @classmethod
    def save_to_db(cls, data):
        """ Save record to the database """
        fancy_id = PushID()

        if not data.f_id:
            data.f_id = fancy_id.next_id()
        db.session.add(data)
        db.session.commit()
        return data.f_id
