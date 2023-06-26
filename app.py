#!/usr/bin/env python

import logging
from flask import Flask, jsonify, request
from slack_bolt import App, Ack
from slack_bolt.adapter.flask import SlackRequestHandler
from bespokebots.slack_blueprints.routes import slack_bp
from bespokebots.gcal_blueprints.routes import gcal_bp
from bespokebots.gcal_blueprints.routes import create_authenticated_client


# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
# Create a Flask web server from the 'app' module name
    app = Flask(__name__)
    app.register_blueprint(slack_bp)
    app.register_blueprint(gcal_bp)

    @app.route('/services/calendar/connect', methods=['GET'])
    def connect_calendar():
    
        logger.info("Received request to connect to Google Calendar")
        calendar_client = create_authenticated_client()
        #get the calendar list
        calendar_list =  calendar_client.get_calendar_list()
        if not calendar_list:
            return "No calendars found"
        else:
            calendars_dict = [entry.to_dict() for entry in calendar_list]   
            return jsonify(calendars_dict)

    logger.info("Slack and GCal blueprints registered, Flask App created")
    return app 


if __name__ == "__main__":
    create_app().run(debug=True)
