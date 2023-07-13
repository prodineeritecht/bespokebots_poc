import uuid
import json
import os
import glob

class User:
    def __init__(self, user_id=None):
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
    def lookup_by_slack_id(slack_user_id):
        user_files = glob.glob('users/*.json')
        for user_file in user_files:
            with open(user_file, 'r') as f:
                data = json.load(f)
                if data.get('slack_user_id') == slack_user_id:
                    # Reconstruct the User object and return it
                    user_id = os.path.basename(user_file).replace('.json', '')
                    user = User()
                    user.user_id = user_id #data.get('user_id')
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
            'state': self.state,
            'credentials': self.credentials,
            'slack_token': self.slack_token,
            'slack_user_id': self.slack_user_id,
            'slack_state': self.slack_state
        }
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

