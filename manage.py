"""The application launch script"""

from flask.cli import FlaskGroup
from app import flask_app
from app.database import db
from db.seeds.user import seed_user
from db.seeds.role_permission import seed_role, seed_permission, \
                                        map_role_to_permission

cli = FlaskGroup(flask_app)


@cli.command("reset_tables")
def reset_tables():
    """
    Drop and re-create all tables
    """
    db.drop_all()
    db.create_all()


@cli.command("seed")
def seed():
    """
    Generate seed/fake data for application database
    """
    seed_role()
    seed_permission()
    map_role_to_permission()
    seed_user()


if __name__ == '__main__':
    cli()
