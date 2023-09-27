#!/usr/bin/env python

import os
import glob
import logging

from flask import Flask, jsonify, request, session
from bespokebots.auth_blueprints.routes import auth_bp
from bespokebots.slack_blueprints.routes import slack_bp
from bespokebots.gcal_blueprints.routes import gcal_bp
from bespokebots.dao.database import db, init_db
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
Session = None

def get_db_session_maker():
    return Session

def create_app(test_config=None):
    global Session
# Create a Flask web server from the 'app' module name
    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'development':
        if os.environ.get('ENABLE_VSCODE_DEBUGGER') == 'true':
            #import ptvsd
            #ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
            print("VS Code debugging DISABLED.")

    app.wsgi_app = ProxyFix(app.wsgi_app) # Fix for running behind a reverse proxy

    if test_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
        app.config["SECRET_KEY"] = "42b612974f9b632ffc0b1da747df528a8d3c66c73d741f6eef8b577d66632509"
    else:
        app.config.from_mapping(test_config)

    Session = init_db(app)
    Migrate(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(slack_bp)
    app.register_blueprint(gcal_bp)
    logger.info("Slack and GCal blueprints registered, Flask App created")


    return app 


if __name__ == "__main__":
    create_app().run(debug=True)


