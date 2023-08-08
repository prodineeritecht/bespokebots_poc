import pytest
import json
from sqlalchemy.types import LargeBinary
from unittest.mock import patch
from unittest.mock import Mock
from datetime import datetime

from bespokebots.services.user_service import UserService

# from tests.base import app, _db, session
from bespokebots.dao import User, ServiceProviders, CredentialStatus, OAuthStateToken
from bespokebots.dao.user_credentials import UserCredentials


class TestUserService:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, db_session):
        self.user = User(username="test_user")
        self.user_service = UserService(db_session)
        self.fake_credentials = json.dumps({"test_key": "test_value"})
        self.workspace_id = "UnitTestingWorkspace"
        self.service_user_id = "test_service_user_id"
        db_session.add(self.user)
        db_session.commit()

        self.user_credentials, self.user_state_token = self.user_service.initialize_user_credentials(
            UserService.lookup_by_user_name("test_user"),
            service_name=ServiceProviders.SLACK.value,
            credentials=self.fake_credentials,
            service_workspace_id=self.workspace_id,
            service_user_id=self.service_user_id,
        )

        yield
        db_session.delete(self.user)
        db_session.commit()

    

    def test_create_user(self, db_session):
        user_service = UserService(db_session)
        user = user_service.create_user(
            username="test_user_name", timezone="test_timezone"
        )
        assert user.username == "test_user_name"
        found_user = UserService.lookup_by_user_name("test_user_name")
        db_session.delete(user)
        assert found_user.id == user.id

    def test_lookup_by_user_name(self):
        assert UserService.lookup_by_user_name(self.user.username).id == self.user.id

    def test_lookup_user_by_state_token(self):
        assert UserService.lookup_user_by_state_token(self.user_state_token).id == self.user.id

    def test_lookup_by_user_name_not_found(self):
        user = UserService.lookup_by_user_name("user_not_found")
        assert user is None

    def test_find_user_by_bad_field_name(self):
        with pytest.raises(AttributeError) as ae:
            UserService.find_user_by_field("bad_field_name", "bad_field_value")
        assert str(ae.value) == "type object 'User' has no attribute 'bad_field_name'"

    def test_state_token_created_with_credentials(self, db_session):
        assert self.user_state_token is not None
        state_token = OAuthStateToken.query.filter_by(value=self.user_state_token).first()
        assert state_token is not None
        assert state_token.value == self.user_state_token
        assert state_token.expires_at > datetime.utcnow()
        creds = self.user_service.get_user_credentials(self.user, ServiceProviders.SLACK.value, self.service_user_id)
        assert creds is not None
        assert creds.oauth_state_token_id == state_token.id

    def test_add_credentials_for_user(self, db_session):
        user_service = UserService(db_session)
        found_user = UserService.lookup_by_user_name("test_user")

        assert found_user.id == self.user.id
        assert found_user.credentials[0] is not None
        new_creds = found_user.credentials[0]
        assert new_creds.service_name == ServiceProviders.SLACK.value
        assert new_creds.service_user_id == self.service_user_id
        assert new_creds.service_workspace_id == self.workspace_id
        assert user_service.decrypt(new_creds.credentials) == self.fake_credentials

    def test_activate_user_credentials(self, db_session):
        #add a set of credentials wity the state.
        creds, state = self.user_service.initialize_user_credentials(
            UserService.lookup_by_user_name("test_user"),
            service_user_id="not_yet_activated",
            service_name=ServiceProviders.GOOGLE.value
            )
        state_token = OAuthStateToken.query.filter_by(value=state).first()

        found_user = UserService.lookup_by_user_name("test_user")
        partial_creds = self.user_service.get_user_credentials(found_user, ServiceProviders.GOOGLE.value)
        assert partial_creds is not None
        assert partial_creds.status == CredentialStatus.INACTIVE.value
        assert partial_creds.credentials is None
        assert partial_creds.date_updated is None

        #create a new set of "credentials" to update the just added incomplete UserCrdentials
        new_creds = json.dumps({"token": "test_value", "redirect_uri": "test_uri"})
        self.user_service.activate_user_credentials(
            UserService.lookup_by_user_name("test_user"),
            service_name=ServiceProviders.GOOGLE.value,
            service_user_id="not_yet_activated",
            state_token=state_token,
            credentials=new_creds
            )
        
        updated_creds = self.user_service.get_user_credentials(found_user, ServiceProviders.GOOGLE.value)
        assert updated_creds is not None
        assert updated_creds.status == CredentialStatus.ACTIVE.value
        assert self.user_service.decrypt(updated_creds.credentials) == new_creds
        assert updated_creds.date_updated is not None

    def test_validate_uniqueness_of_user_credentials(self, db_session):
        pass

    def test_find_user_by_service_user_id(self):
        found_user = UserService.lookup_by_service_user_id(
            ServiceProviders.SLACK.value, self.service_user_id
        )
        assert found_user.id == self.user.id

    def test_revoke_user_credentials(self, db_session):
        user_service = UserService(db_session)
        found_user = UserService.lookup_by_user_name("test_user")
        assert found_user.id == self.user.id
        assert found_user.credentials[0] is not None
        user_service.revoke_user_credentials(found_user.credentials[0])
        assert found_user.credentials[0].status == CredentialStatus.REVOKED.value

    def test_get_user_credentials(self, db_session):
        # add a new set of credentials to the test user's credentials list
        fake_creds = json.dumps({"token": "test_value", "redirect_uri": "test_uri"})
        google_creds = self.user_service.initialize_user_credentials(
            UserService.lookup_by_user_name("test_user"),
            service_name=ServiceProviders.GOOGLE.value,
            credentials=fake_creds,
            service_user_id="google_service_user_id",
        )
        found_credentials = self.user_service.get_user_credentials(
            user=self.user,
            service_name=ServiceProviders.GOOGLE.value,
            service_user_id="google_service_user_id",
        )
        assert found_credentials is not None
        assert found_credentials.service_name == ServiceProviders.GOOGLE.value
        assert found_credentials.service_user_id == "google_service_user_id"
        assert found_credentials.service_workspace_id is None
        assert self.user_service.decrypt(found_credentials.credentials) == fake_creds

    def test_delete_user(self, db_session):
        delete_user = self.user_service.create_user(
            username="delete_user_name", timezone="test_timezone"
        )
        found_user = UserService.lookup_by_user_name("delete_user_name")
        assert found_user.id == delete_user.id
        self.user_service.delete_user(found_user)
        assert UserService.lookup_by_user_name("delete_user_name") is None
