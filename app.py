#!/usr/bin/env python

import os
import glob
import logging
import ptvsd
from flask import Flask, jsonify, request, session
from slack_bolt import App, Ack
from slack_bolt.adapter.flask import SlackRequestHandler
from bespokebots.auth_blueprints.routes import auth_bp
from bespokebots.slack_blueprints.routes import slack_bp
from bespokebots.gcal_blueprints.routes import gcal_bp
from bespokebots.gcal_blueprints.routes import create_authenticated_client
from bespokebots.models.user import User
from werkzeug.middleware.proxy_fix import ProxyFix



# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# This is temporary to get past a "chicken or the egg" problem.
# I need to finish out the full Google OAuth flow, and want to introduce the concept of a User
# However, I don't yet want to take on the complexity of full user management since I am still just
# prototyping. So, I am going to create a single user and store it in the session.
# This should also be very easy to rip out and replace in the near future when I have settled on a 
# user management strategy/solution.
def load_or_create_user():
    logger.info("Loading or creating user")
    user_files = glob.glob("users/*.json")
    if not user_files:
        # No user files exist, so create a new user
        logger.info("No user files found, creating a new user")
        user = User()
        user._save()
    else:
        # Load the first user file we find  
        logger.info("Found user file, loading user")
        user_id = os.path.basename(user_files[0]).replace('.json', '')
        user = User(user_id=user_id)

    return user

def create_app():
# Create a Flask web server from the 'app' module name
    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'development':
        if os.environ.get('ENABLE_VSCODE_DEBUGGER') == 'true':
            ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
            print("VS Code debugging enabled.")

    app.wsgi_app = ProxyFix(app.wsgi_app) # Fix for running behind a reverse proxy

    app.config["SECRET_KEY"] = "42b612974f9b632ffc0b1da747df528a8d3c66c73d741f6eef8b577d66632509"
   
    # @app.before_request
    # def load_user_into_session():
    #     logger.info(f"Calling before_request handler: load_user_into_session session[user_id]: {session.get('user_id')}")
    #     if 'user_id' not in session:
    #         user = load_or_create_user()
    #         session['user_id'] = user.user_id

    app.register_blueprint(auth_bp)
    app.register_blueprint(slack_bp)
    app.register_blueprint(gcal_bp)
    logger.info("Slack and GCal blueprints registered, Flask App created")


    return app 


if __name__ == "__main__":
    create_app().run(debug=True)


    