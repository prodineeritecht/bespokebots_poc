import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo
from todoist_api_python.models import Project
import json

from bespokebots.services.agent.todoist_tools import (ViewProjectsTool,
                                                      CreateProjectTool)

from bespokebots.models.tools.todoist import TodoistProject 


def test_create_new_project(project):
    project_name = "Test Project"
    assert project is not None
    assert project['name'] == project_name

    #make sure it's in the list of projects
    view_tool = ViewProjectsTool()
    projects = view_tool.run({"project_id": str(project['id'])})
    assert projects is not None
    assert len(projects['projects']) > 0
    assert projects['projects'][0]['name'] == project_name

def test_create_new_project_with_parent(project, child_project):
    project_name = "Test Child Project"
    parent_project_name = "Test Project"
    assert project is not None
    assert project['name'] == parent_project_name

    assert child_project is not None
    assert child_project['name'] == project_name
    assert child_project['parent_id'] == project['id']


def test_create_project_with_color(lime_green_project):
    project_name = "Test Project"
    
    assert lime_green_project is not None
    assert lime_green_project['name'] == project_name
    assert lime_green_project['color'] == "lime_green"

    #make sure it's in the list of projects
    view_tool = ViewProjectsTool()
    projects = view_tool.run({"project_id": str(lime_green_project['id'])})
    assert projects is not None
    assert len(projects['projects']) > 0
    assert projects['projects'][0]['name'] == project_name
    assert projects['projects'][0]['color'] == "lime_green"