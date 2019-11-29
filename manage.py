import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main.model import user

# creates the application instance with the required parameter
# dev, prod, test
# if none is set in the environment variable, the default dev is used
from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

# marks functions executable from the command line
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()