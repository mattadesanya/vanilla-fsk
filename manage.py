"""The application launch script"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import flask_app
from app.database import db
from db.seeds.user import seed_user


migrate = Migrate(flask_app, db)
manager = Manager(flask_app)
manager.add_command('db', MigrateCommand)


@manager.command
def reset_tables():
    """
    Drop and re-create all tables
    """
    db.drop_all()
    db.create_all()


@manager.command
def seed():
    """
    Generate seed/fake data for application database
    """
    seed_user()


if __name__ == '__main__':
    manager.run()
