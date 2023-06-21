import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo
from todoist_api_python.models import Project
import json

from bespokebots.services.agent.todoist_tools import (CreateTaskTool, 
                                                      ViewProjectsTool)

from bespokebots.models.tools.todoist import TodoistProject

def test_create_task_only_content(create_task_tool, task):
    
    assert task is not None
    project_id = task['project_id']
    project = create_task_tool.todoist_client.get_project(project_id)
    assert project.name == "Inbox"


def test_create_task_with_project(project_task, project_id):
    #personal project id
    assert project_task is not None
    assert project_task['project_id'] == project_id

    #make sure the task is in the project
    view_tool = ViewProjectsTool()
    projects = view_tool.run({"project_id": project_id})
    project = projects['projects'][0]
    assert project is not None
    assert len(project['tasks']) > 0
    assert project['tasks'][0]['id'] == project_task['id']

