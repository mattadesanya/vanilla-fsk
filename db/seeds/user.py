from app.util.db_util import DbUtil as db
from app.models.user import User
from faker import Faker

fake = Faker()


def seed_user():
    # create one admin user
    user = User(username='matt',
                password='12345',
                role='admin')

    db.save_to_db(user)

    # add 9 normal users
    for i in range(9):
        username = fake.simple_profile().get('username')
        user = User(username=username, password='12345')
        db.save_to_db(user)
