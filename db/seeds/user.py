from app.util.db import DbUtil as db
from app.models.user import User
from faker import Faker

fake = Faker()


def seed_user():
    for i in range(10):
        # add one admin user and two other users
        username = fake.simple_profile().get("username")
        user = User(username=username, password="12345")
        db.save_to_db(user)
