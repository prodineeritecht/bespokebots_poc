import uuid
import json
from datetime import datetime
import os
import glob
import base64
import logging
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from zoneinfo import ZoneInfo
from slack_sdk.oauth.installation_store.models.installation import Installation
from bespokebots.dao import (
    User,
    UserCredentials,
    ServiceProviders,
    CredentialStatus,
    OAuthStateToken,
)

logging.basicConfig(level=logging.INFO)
# Initialize the logger
logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, session):
        self.session = session
        key = os.environ.get("USER_CREDENTIALS_KEY")
        if not key:
            raise ValueError("Missing environment variable: USER_CREDENTIALS_KEY")
        self.encryption_key = self.encode_key(key)

    def encode_key(self, b64_key):
        return base64.b64decode(b64_key.encode())

    def create_user(self, username, timezone=ZoneInfo("America/New_York").key):
        user = User(username=username, timezone=timezone)
        self.session.add(user)
        self.session.commit()
        return user

    def delete_user(self, user):
        self.session.delete(user)
        self.session.commit()

    def encrypt(self, data) -> bytes:
        cipher = AES.new(self.encryption_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
        iv = cipher.iv
        return iv + ct_bytes  # Return as bytes

    def decrypt(self, encrypted_data) -> str:
        try:
            iv = encrypted_data[:16]
            ct = encrypted_data[16:]
            cipher = AES.new(self.encryption_key, AES.MODE_CBC, iv=iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            return pt.decode("utf-8")
        except (ValueError, KeyError):
            print("Incorrect decryption")

    def create_state_token(self, user_id) -> OAuthStateToken:
        state_token = OAuthStateToken(user_id=user_id)
        self.session.add(state_token)
        self.session.commit()
        return state_token

    def initialize_user_credentials(
        self,
        user: User,
        service_name,
        service_user_id=None,
        credentials=None,
        service_workspace_id=None,
        state_token: OAuthStateToken = None,
    ):
        # Create a new state token
        if not state_token:
            state_token = OAuthStateToken(user_id=user.id)
            self.session.add(state_token)
            # The state token value isn't created until db save, so we need to commit first
            self.session.commit()

        user_credentials = UserCredentials(
            user_id=user.id,
            service_name=service_name,
            credentials=self.encrypt(credentials) if credentials else None,
            service_user_id=service_user_id,
            service_workspace_id=service_workspace_id,
            oauth_state_token_id=state_token.id,
        )

        self.session.add(user_credentials)
        self.session.commit()
        return user_credentials, state_token.value

    def find_user_credentials_by_state_token(self, state_token):
        # We need the join here because we only have the state token value, not its id in the database
        return (
            self.session.query(UserCredentials)
            .join(OAuthStateToken)
            .filter(OAuthStateToken.value == state_token)
            .first()
        )

    def get_user_credentials(
        self, user: User, service_name: str, service_user_id: str = None
    ):
        # Commit any unsaved changes to the user instance
        if user in self.session.dirty:
            self.session.commit()

        # make sure we have the most up to date version of the user instance
        self.session.refresh(user)

        # if a service_user_id isn't provided, look up all credentials for the service
        # If there is only one credential, return it. If there are multiple, raise an error
        # indicating that we can't determine the correct credential to return
        if not service_user_id:
            logger.info(f"Looking up credentials for user {user.id} and service {service_name}, no service_user_id provided")
            user_creds = [
                creds
                for creds in user.credentials
                if creds.service_name == service_name
                and creds.status == CredentialStatus.ACTIVE.value
            ]
            logger.info(f"Found {len(user_creds)} credentials for user {user.id} and service {service_name}")
            if len(user_creds) > 1:
                raise ValueError(
                    f"Multiple credentials found for user {user.id} and service {service_name}. Please provide a service_user_id"
                )
            else:
                user_creds = user_creds.pop()

        else:
            logger.info(f"Looking up credentials for user {user.id} and service {service_name}, service_user_id {service_user_id}")
            user_creds = [
                creds
                for creds in user.credentials
                if creds.service_name == service_name
                and creds.service_user_id == service_user_id
                and creds.status == CredentialStatus.ACTIVE.value
            ].pop()

        return user_creds

    def activate_user_credentials(
        self,
        user: User,
        state_token_value: str,
        service_name: ServiceProviders,
        service_user_id: str,
        credentials: str,
    ):
        user_credentials = self.find_user_credentials_by_state_token(state_token_value)
        state_token = OAuthStateToken.find_by_value(value=state_token_value)

        if not user_credentials:
            raise ValueError(
                f"User credentials not found for user {user.id} and service {service_name}"
            )

        if state_token.expires_at < datetime.utcnow():
            raise ValueError(
                f"State token has expired for user {user.id} and service {service_name}"
            )

        # This case is actually validated by the fact that the user credentials were found
        # with the state token, so we know that this if will always evaluate to true. going to
        # comment it out, but leave to sort of explicitly point out that this case is handled.
        # if state_token.id != user_credentials.oauth_state_token_id:
        #     raise ValueError(
        #         f"State token does not match user credentials for user {user.id} and service {service_name}"
        #     )

        user_credentials.credentials = self.encrypt(credentials)
        user_credentials.status = CredentialStatus.ACTIVE.value
        user_credentials.date_updated = datetime.now(ZoneInfo(user.timezone))
        user_credentials.service_user_id = service_user_id
        self.session.commit()
        return user_credentials

    def revoke_user_credentials(self, user_credentials: UserCredentials):
        user_credentials.status = CredentialStatus.REVOKED.value
        self.session.commit()

    def validate_state_token(self, state_token_value: str):
        state_token = OAuthStateToken.find_by_value(value=state_token_value)
        if not state_token:
            logger.warn(f"State token {state_token_value} not found")
            return False

        if state_token.expires_at < datetime.utcnow():
            logger.warn(f"State token {state_token_value} has expired")
            return False

        return True

    @staticmethod
    def lookup_by_user_id(user_id, session=None):
        return UserService.find_user_by_field("id", user_id, session=session)

    @staticmethod
    def lookup_by_service_user_id(service_name, service_user_id, session=None):
        return User.find_by_credential_service_id(
            service_name, service_user_id, session=session
        )

    @staticmethod
    def lookup_by_user_name(user_name):
        return User.find_by_user_name(user_name)

    @staticmethod
    def find_user_by_field(field, value, session=None):
        return User.find_by_field_name(field, value, session=session)

    @staticmethod
    def lookup_user_by_state_token(state_token):
        return User.find_by_state_token(state_token)
