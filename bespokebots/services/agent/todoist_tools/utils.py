from todoist_api_python.api import TodoistAPI
import os


def _get_token_from_env() -> str:
    """Get the Todoist API token from the environment."""
    api_token = os.environ["TODOIST_API_KEY"]
    if not api_token:
        raise ValueError("No API token found in the environment.")
    return api_token



def build_todoist_client(api_token: str = None) -> TodoistAPI:
    """Build a Todoist client."""
    if not api_token:
        api_token = _get_token_from_env()

    client = TodoistAPI(api_token)
    return client
