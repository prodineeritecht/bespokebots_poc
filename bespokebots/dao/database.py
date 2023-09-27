from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
import os

#create the SQLAlchemy object
db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.init_app(app)
        Session = scoped_session(sessionmaker(bind=db.engine))
        return Session

def create_session():
    db_url = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    return Session    