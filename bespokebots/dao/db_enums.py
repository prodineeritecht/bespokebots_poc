from enum import Enum

class ServiceProviders(Enum):
    GOOGLE = "Google"
    SLACK = "Slack"
    TODOIST = "Todoist"

class CredentialStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    REVOKED = "Revoked"