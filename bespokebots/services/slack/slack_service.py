from slack_bolt import App, Ack
from slack_sdk.errors import SlackApiError
import logging

from bespokebots.models.communication_services import CommunicationService
from bespokebots.models.communication_channels import CommunicationChannel


class SlackService(CommunicationService):
    def __init__(self, slack_app: App, logger: logging.Logger):
        self.slack_app = slack_app
        self.logger = logger

    def send_message(self, channel: str, text: str):
        try:
            print(f"Sending message to {channel}:\n {text}")
            response = self.slack_app.client.chat_postMessage(
                channel=channel,
                text=text,
            )
            #assert response["message"]["text"] == text
        except SlackApiError as e:
            self.logger.error(f"Error posting message: {e}")

    def send_formatted_message(self, channel: str, response: dict):
        """Send a formatted message to a Slack channel. Useful for sending Block Kit based responses."""
        
        pass

    def send_message_with_blocks(self, channel: str, blocks: list):
        try:
            response = self.slack_app.client.chat_postMessage(
                channel=channel,
                blocks=blocks,
            )
            assert response["message"]["text"] == text
        except SlackApiError as e:
            self.logger.error(f"Error posting message: {e}")


class SlackChannel(CommunicationChannel):
    """A Slack channel that can be used to send and receive messages."""
    service: SlackService

    def __init__(self, channel_id: str, service: SlackService):
        self.channel_id = channel_id
        self.service = service

    def send_response(self, response: str):
        self.service.send_message(self.channel_id, response)

    def format_response(self, response: str) -> str:
        #Based on the passed in, figure out if there is an appropriate block kit template to use
        #If there is, use it. If not, just send the text
        return response

