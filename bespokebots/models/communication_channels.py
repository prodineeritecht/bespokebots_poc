
from abc import ABC, abstractmethod

from bespokebots.models.communication_services import CommunicationService

class CommunicationChannel(ABC):
    """Base abstract class for communication channels. Communications
    channels will be services such as Slack, Discord, SMS, email, etc."""

    service: CommunicationService

    @abstractmethod
    def send_response(self, response: str):
        """Sends a response to the user via this communication channel."""

    @abstractmethod
    def format_response(self, response: str) -> str:
        """Formats the response into a format that is appropriate for this communication channel."""
