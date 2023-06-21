from __future__ import annotations

from typing import TYPE_CHECKING
from pydantic import Field
from langchain.tools.base import BaseTool
from todoist_api_python.api import TodoistAPI
from bespokebots.services.agent.todoist_tools.utils import build_todoist_client

class TodoistBaseTool(BaseTool):
    todoist_client: TodoistAPI = Field(default_factory=build_todoist_client)

    @classmethod
    def from_todoist_client(
        cls, todoist_client: TodoistAPI
    ) -> TodoistBaseTool:
        return cls(todoist_client=todoist_client)
