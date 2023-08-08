import pytest
from unittest.mock import patch, MagicMock
from urllib.parse import unquote
import json
import uuid
import types
import secrets
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from bespokebots.services.google_calendar import (
    GoogleCalendarClient,
    GoogleCalendarEvent,
)

from bespokebots.dao import (
    User,
    UserCredentials,
    ServiceProviders,
    CredentialStatus,
    OAuthStateToken,
)
from bespokebots.services.user_service import UserService


class TestGoogleCalendarClientOauthFlows:
    scopes = ["https://www.googleapis.com/auth/calendar"]
    fake_client_creds = "fakecreds.json"
    google_auth_url = "https://accounts.google.com/o/oauth2/auth"

    # @pytest.fixture
    # def mock_credentials(self):
    #     with patch("google.oauth2.credentials.Credentials") as mock_Credentials:
    #         yield mock_Credentials

    # @pytest.fixture
    # def mock_flow(self):
    #     with patch("google_auth_oauthlib.flow.Flow") as mock_Flow:
    #         yield mock_Flow

    @patch("jwt.decode")
    @patch("google_auth_oauthlib.flow.Flow", autospec=True)
    def test_google_cal_client_oauth_flow(
        self, mock_flow, mock_jwt_decode, db_session, test_user
    ):
        # Create a mock Flow
        user_service = UserService(db_session)
        user = test_user
        mock_flow_instance = mock_flow.from_client_config.return_value

        mock_flow_instance.authorization_url.return_value = (
            self.google_auth_url,
            "mock_state",
        )

        # Create an instance of your GoogleCalendarClient
        google_client = GoogleCalendarClient(
            self.fake_client_creds, self.scopes, user_service=user_service, user=user, flow=mock_flow_instance
        )  # Pass a None user_service

        # Use the mocked Flow instance to initiate the OAuth flow with Google
        #with mock_flow:
        authorization_url = google_client.initiate_oauth_flow(
            "https://example.com/callback"
        )

        # Assertions based on your implementation and expected behavior
        assert authorization_url == self.google_auth_url
        
        assert len(user.credentials) == 1
        creds = user.credentials[0]
        assert creds.status == CredentialStatus.INACTIVE.value
        assert creds.service_name == ServiceProviders.GOOGLE.value
        assert creds.oauth_state_token is not None
        assert creds.oauth_state_token_id is not None
        assert creds.credentials is None

        state_token = creds.oauth_state_token
        assert state_token.user_id == user.id

        # The Initiate OAUth step has worked, now verify that when the
        # callback request is received by bespoke bots, our GCal client
        # is able to retrieve the user's credentials and store them
        fake_jwt_token = (
            "eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwMjMtMDctMzEifQ.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ."
            "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        )

        fake_service_id = str(uuid.uuid4())
        mock_jwt_decode.return_value = {'sub' : fake_service_id}

        fake_credentials = {
            "token": "ya29.a0AbVbY6PyRdM9cncfUR3QazVjYe0_KV5XA0qfH_9MPpzRv3EULWEn5E63B4Nlna0bB81IT3C_RwTw_FDmSc-ymiuHN52WBRPsV5-rdkwz16d7XID2bVb3JPBon4spIvajqSXAaA-L4W_GInarF-bMWnIONZCdaCgYKAQQSARASFQFWKvPlE_827v4YUMppudLREyDwdQ0163",
            "refresh_token": "1//01-F_gA3kVUy0CgYIARAAGAESNwF-L9IrCQV1Hr_8OKOdg93vZAZgOKFdoxgVEJHPdZNdOe7BLmikgL2wEWdcs-YOFDJCssYIvQo",
            "token_uri": "https://oauth2.googleapis.com/token",
            "client_id": "38992558726-n9en7smp0r5320gd86o623klba3jsjga.apps.googleusercontent.com",
            "client_secret": "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",
            "scopes": [
                "https://www.googleapis.com/auth/calendar"
            ],
            "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwMjMtMDctMzEifQ.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ."
            }
        #make it so the fake credentials can be accessed with dot notation
        fake_credentials_obj = types.SimpleNamespace(**fake_credentials)
        
        mock_flow_instance.fetch_token.return_value = {
            'access_token': secrets.token_urlsafe(32),
            'token_type': 'Bearer',
            'expires_in': 3600,
            'refresh_token': secrets.token_urlsafe(16),
            'id_token': fake_jwt_token  # Add the fake JWT token here
        }

        
        #mock_flow_instance.credentials.id_token = fake_jwt_token
        mock_flow_instance.credentials = fake_credentials_obj

       # mock_credentials.from_authorized_user_info.return_value = fake_credentials
        fake_auth_code = secrets.token_urlsafe(32)
        
        #reinstantiate the client since this flow spans two separate routes.
        google_client = GoogleCalendarClient(
            self.fake_client_creds, self.scopes, user_service=user_service, user=user, flow=mock_flow_instance
        )
        
        google_client.authenticate_oauth(
            authorization_url + f"&code={fake_auth_code}",
            "https://example.com/callback",
            state_token.value
        )

        # verify the user now has an active set of credentials authorizing bespokebots to access
        # their calendar on their behalf
        assert len(user.credentials) == 1  # verify that we didn't add a new set.
        updated_creds = user.credentials[0]
        assert updated_creds.user_id == user.id
        assert updated_creds.status == CredentialStatus.ACTIVE.value
        assert updated_creds.service_user_id == fake_service_id
        decrypted_creds_json = json.loads(user_service.decrypt(updated_creds.credentials)) 
        assert decrypted_creds_json.get("token") == fake_credentials.get("token")
        assert decrypted_creds_json.get("refresh_token") == fake_credentials.get("refresh_token")
        assert decrypted_creds_json.get("token_uri") == fake_credentials.get("token_uri")
        assert decrypted_creds_json.get("client_id") == fake_credentials.get("client_id")
        assert decrypted_creds_json.get("client_secret") == fake_credentials.get("client_secret")


if __name__ == "__main__":
    pytest.main()
