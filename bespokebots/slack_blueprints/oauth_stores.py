# this module will have the custom Installation and State stores for the Slack OAuth implementation
from logging import Logger
from slack_sdk.oauth.installation_store import InstallationStore
from slack_sdk.oauth.state_store import OAuthStateStore
from bespokebots.dao import UserCredentials, OAuthStateToken
from bespokebots.dao.database import db
from bespokebots.services.user_service import UserService
from sqlalchemy.orm import Session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomSQLAlchemyInstallationStore(InstallationStore):

    @property
    def logger(self) -> Logger:
        return logger


    def __init__(self, user_service: UserService = None, ):
        self.user_service = user_service if user_service else UserService(db.session)

    def save(self, installation, bb_user_id: int):
        self.user_service.from_slack_installation_to_user_credentials(bb_user_id, installation)
           

    def find_installation(
        self,
        *,
        enterprise_id=None,
        team_id=None,
        user_id=None,
        is_enterprise_install=None
    ):
        query = self.session.query(UserCredentials)
        # add conditions to the query based on method parameters
        return query.first()

    def delete_installation(self, *, enterprise_id=None, team_id=None, user_id=None):
        query = self.session.query(UserCredentials)
        # add conditions to the query based on method parameters
        query.delete()
        self.session.commit()

    def delete_all(self, enterprise_id=None, team_id=None):
        query = self.session.query(UserCredentials)
        # add conditions to the query based on method parameters
        query.delete()
        self.session.commit()


class CustomSQLAlchemyStateStore(OAuthStateStore):
    def __init__(self, session: Session, expiration_seconds: int):
        self.session = session
        self.expiration_seconds = expiration_seconds

    def issue(self):
        state = OAuthStateToken(
            # Define properties as needed
        )
        self.session.add(state)
        self.session.commit()
        return state.token

    def consume(self, state):
        query = self.session.query(OAuthStateToken).filter_by(token=state)
        record = query.first()
        if record:
            self.session.delete(record)
            self.session.commit()

