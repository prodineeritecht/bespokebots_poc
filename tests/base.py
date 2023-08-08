# tests/base.py
import pytest
from app import create_app
from bespokebots.dao.database import db

@pytest.fixture(scope='session')
def app_fixture():
    """Session-wide test `Flask` application."""
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    }
    app = create_app(test_config=test_config)
    return app

@pytest.fixture(scope='session')
def _db(app_fixture):
    """Session-wide test database."""
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()

@pytest.fixture(scope='function')
def db_session(_db, request):
    """Creates a new database session for a test."""
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
