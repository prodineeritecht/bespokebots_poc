from abc import ABC, abstractmethod

class CommunicationService(ABC):

    @abstractmethod
    def send_message(self, channel: str, text: str):
        pass

    @abstractmethod
    def send_formatted_message(self, channel: str, response: dict):
        pass



