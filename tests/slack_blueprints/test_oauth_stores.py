import pytest
import json
from sqlalchemy.types import LargeBinary
from unittest.mock import patch
from unittest.mock import Mock
from datetime import datetime

from bespokebots.services.user_service import UserService
from bespokebots.dao import User, ServiceProviders, CredentialStatus
from bespokebots.slack_blueprints.oauth_stores import CustomSQLAlchemyInstallationStore, 

class TestOauthStores:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, db_session):
        self.user = User(username="test_user")
        self.user_service = UserService(db_session)
        self.fake_credentials = json.dumps({"test_key": "test_value"})
        self.workspace_id = "UnitTestingWorkspace"
        self.service_user_id = "test_service_user_id"
        db_session.add(self.user)
        db_session.commit()

        self.user_credentials = self.user_service.initialize_user_credentials(
            UserService.lookup_by_user_name("test_user"),
            service_name=ServiceProviders.SLACK.value,
            state="test_state",
            credentials=self.fake_credentials,
            service_workspace_id=self.workspace_id,
            service_user_id=self.service_user_id,
        )

        yield
        db_session.delete(self.user)
        db_session.commit()

    def test_save_slack_installation():
        pass

    def test_find_slack_installation():
        pass

    def test_delete_slack_installation():
        pass

    def test_save_state_token():
        pass

