import uuid
import json
import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)

class User:
    def __init__(self,user_name, user_id=None):
        self.user_name = user_name
        self.user_id = user_id or str(uuid.uuid4())
        self.file_path = f"users/{self.user_id}.json"
        self.state = None
        self.credentials = None
        self.slack_token = None
        self.slack_state = None
        self.slack_user_id = None

        # Load user data from file if it exists
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.state = data.get('state')
                self.credentials = data.get('credentials')
                self.slack_token = data.get('slack_token')
                self.slack_state = data.get('slack_state')
                self.slack_user_id = data.get('slack_user_id')
                self.user_id = data.get('user_id')

    def save_state(self, state):
        self.state = state
        self._save()

    def retrieve_state(self):
        return self.state

    def save_credentials(self, credentials):
        self.credentials = credentials
        self._save()

    def retrieve_credentials(self):
        return self.credentials

    def set_slack_token(self, slack_token, state=None):
        self.slack_token = slack_token
        if state is not None:
            self.state = state
        self._save()

    def get_slack_token(self):
        return self.slack_token

    def save_creds_and_state(self, credentials, state):
        self.credentials = credentials
        self.state = state
        self._save()

    @staticmethod
    def lookup_by_user_id(user_id):
        return User.find_user_by_field('user_id', user_id)
    
    @staticmethod
    def lookup_by_slack_id(slack_user_id):
        return User.find_user_by_field('slack_user_id', slack_user_id)  
    
    @staticmethod
    def lookup_by_user_name(user_name): 
        return User.find_user_by_field('user_name', user_name)

    @staticmethod
    def find_user_by_field(field, value):
        user_files = glob.glob('users/*.json')
        logger.info(f"Found {len(user_files)} user files")
        for user_file in user_files:
            logger.info(f"Checking {user_file}")
            with open(user_file, 'r') as f:
                data = json.load(f)
                logger.info(f"Checking {data.get(field)} against {value}")
                if data.get(field) == value:
                    # Reconstruct the User object and return it
                    logger.info(f"Found a match for {value}")
                    user_id = os.path.basename(user_file).replace('.json', '')
                    user = User(data.get('user_name'))
                    user.user_id = user_id #data.get('user_id')
                    user.user_name = data.get('user_name')
                    user.credentials = data.get('credentials')
                    user.state = data.get('state')
                    user.slack_user_id = data.get('slack_user_id')
                    user.slack_state = data.get('slack_state')
                    user.slack_token = data.get('slack_token')
                    return user
        return None
    
    def _save(self):
        data = {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'state': self.state,
            'credentials': self.credentials,
            'slack_token': self.slack_token,
            'slack_user_id': self.slack_user_id,
            'slack_state': self.slack_state
        }
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

