import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo
from todoist_api_python.models import Project
import json

from bespokebots.services.agent.todoist_tools import ViewProjectsTool
from bespokebots.models.tools.todoist import TodoistProject

def test_view_projects():
    tool = ViewProjectsTool()
    projects = tool.run({})
    assert len(projects) > 0

    project_zero = projects['projects'][0]
    assert isinstance(project_zero, dict)
    print(project_zero["name"])
    print(project_zero["id"])
    print(project_zero["url"])
    assert project_zero["name"] is not None
    

    declutter_project = next((p for p in projects['projects'] if p['name'] == "Office Decluttering"), None)
    assert declutter_project is not None
    assert len(declutter_project['tasks']) > 0

    
    json_projects = json.dumps(projects, indent=4)
    #print(json_projects)

def test_view_projects_with_project_id():
    tool = ViewProjectsTool()
    project_id = "2054677608"
    project = tool.run({"project_id": project_id})

    assert project is not None
    assert len(project["projects"]) == 1
    personal = project["projects"][0]
    assert personal['name'] == "Personal"

def test_view_project_by_name():
    tool = ViewProjectsTool()
    project_name = "Personal"
    project = tool.run({"project_names": [project_name]})

    assert project is not None
    assert len(project["projects"]) == 1
    personal = project["projects"][0]
    assert personal['name'] == "Personal"

def test_view_multiple_projects_by_name():
    tool = ViewProjectsTool()
    project_names = ["Personal", "Office Decluttering"]
    project = tool.run({"project_names": project_names})

    assert project is not None
    assert len(project["projects"]) == 2
    personal = project["projects"][0]
    assert personal['name'] == "Personal"
    declutter = project["projects"][1]
    assert declutter['name'] == "Office Decluttering"
    