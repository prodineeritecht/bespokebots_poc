from slack_bolt import App, Ack
from slack_sdk.errors import SlackApiError
import logging


class SlackService:
    def __init__(self, slack_app: App, logger: logging.Logger):
        self.slack_app = slack_app
        self.logger = logger

    def send_message(self, channel: str, text: str):
        try:
            response = self.slack_app.client.chat_postMessage(
                channel=channel,
                text=text,
            )
            assert response["message"]["text"] == text
        except SlackApiError as e:
            self.logger.error(f"Error posting message: {e}")

    def send_message_with_blocks(self, channel: str, blocks: list):
        try:
            response = self.slack_app.client.chat_postMessage(
                channel=channel,
                blocks=blocks,
            )
            assert response["message"]["text"] == text
        except SlackApiError as e:
            self.logger.error(f"Error posting message: {e}")

