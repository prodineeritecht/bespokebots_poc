from datetime import datetime
import json
from bespokebots.dao.database import db
from bespokebots.dao.db_enums import CredentialStatus


class UserCredentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_name = db.Column(db.String(80), nullable=False)
    credentials = db.Column(db.LargeBinary, nullable=True) #encrypted field
    service_user_id = db.Column(db.String, nullable=False)
    service_workspace_id = db.Column(db.String, nullable=True) #this is the team_id from the slack API
    service_workspace_name = db.Column(db.String, nullable=True) #this is the team_name from the slack API
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True) 
    status = db.Column(db.String(80), nullable=False, default=CredentialStatus.INACTIVE.value)

    oauth_state_token_id = db.Column(db.Integer, db.ForeignKey('oauth_state_tokens.id'), nullable=True)
    oauth_state_token = db.relationship("OAuthStateToken", back_populates="credentials")


  