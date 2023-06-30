import os 
from flask import Flask, jsonify, request
from slack_bolt import App, Ack
from celery import Celery
from typing import Optional
import logging
from bespokebots.services.slack.slack_service import SlackService
from bespokebots.services.agent import BespokeBotAgent
from bespokebots.services.chains.templates import (
    STRUCTURED_CHAT_PROMPT_PREFIX, 
    STRUCTURED_CHAT_PROMPT_SUFFIX
    )

broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672/")
celery = Celery('my_project', broker=broker_url)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


slack_app = App(
    token=os.environ.get("BESPOKE_BOTS_SLACK_BOT_TOKEN"),
    signing_secret= os.environ.get("BESPOKE_BOTS_SLACK_SIGNING_SECRET")
)

agent = BespokeBotAgent(ai_name="BespokeBot")
agent.initialize_agent(prefix=STRUCTURED_CHAT_PROMPT_PREFIX, suffix=STRUCTURED_CHAT_PROMPT_SUFFIX)

        
@celery.task
def process_slack_message(user_id: str, channel_id: str, text: str):
    # Here is where you will do your long-running task processing the slack message
    logger.info(f"Celery Task for slack message from user {user_id} in channel {channel_id}")
    slack_handlers = SlackService(slack_app, logger)
    response_text = agent.run_agent(text)

    # Once you have the results, you can send a message back to the user
    slack_handlers.send_message(channel_id, response_text)
