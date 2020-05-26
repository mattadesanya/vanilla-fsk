"""The application launch script"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from app.database import db


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def reset_tables():
    """
    Drop and re-create all tables
    """
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
