from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from datetime import timedelta
from bespokebots.dao.database import db
from bespokebots.dao.db_enums import CredentialStatus
import secrets

class OAuthStateToken(db.Model):
    __tablename__ = "oauth_state_tokens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    value = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() + timedelta(minutes=10))

    credentials = db.relationship("UserCredentials", uselist=False, back_populates="oauth_state_token")

    __table_args__ = (db.UniqueConstraint("value", name="unique_value"),)

    def __init__(self, user_id):
        self.user_id = user_id
        self.value = secrets.token_hex(16)
        self.created_at = datetime.utcnow()
        self.expires_at = self.created_at + timedelta(minutes=10)

    @classmethod
    def find_by_value(cls, value):
        return cls.query.filter_by(value=value).first()
