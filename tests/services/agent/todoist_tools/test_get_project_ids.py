import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo
from todoist_api_python.models import Project
import json

from bespokebots.services.agent.todoist_tools import GetProjectIdsTool
from bespokebots.models.tools.todoist import TodoistProject

def test_get_a_single_project_id():
    tool = GetProjectIdsTool()
    project_name = "Personal"
    project_id_map = tool.run({"project_names": [project_name]})
    assert project_id_map is not None
    assert len(project_id_map) == 1
    assert project_id_map[0]['project_id'] == "2054677608"
    assert project_id_map[0]['project_name'] == "Personal"

def test_get_multiple_project_ids():
    tool = GetProjectIdsTool()
    project_names = ["Personal", "Bespoke Bots"]
    project_id_map = tool.run({"project_names": project_names})
    assert project_id_map is not None
    assert len(project_id_map) == 2
    assert project_id_map[0]['project_id'] == "2054677608"
    assert project_id_map[0]['project_name'] == "Personal"
    assert project_id_map[1]['project_id'] == "2315024262"
    assert project_id_map[1]['project_name'] == "Bespoke Bots"

def test_get_all_project_ids():
    #this test might be brittle if I just couple it to the number of projects.  I will instead
    #assert that a few specific projects are in the list
    tool = GetProjectIdsTool()
    project_id_map = tool.run({"project_names": []})

    assert project_id_map is not None
    assert len(project_id_map) > 0

    declutter_project = next((p for p in project_id_map if p['project_name'] == "Office Decluttering"), None)
    assert declutter_project is not None

    inbox_project = next((p for p in project_id_map if p['project_name'] == "Inbox"), None)
    assert declutter_project is not None

