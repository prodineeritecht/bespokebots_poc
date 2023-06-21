import pytest
from unittest.mock import patch
from unittest.mock import Mock
import datetime
from zoneinfo import ZoneInfo
from todoist_api_python.models import Project
import json

from bespokebots.services.agent.todoist_tools import (CreateTaskTool, 
                                                      ViewProjectsTool,
                                                      CloseTaskTool)

from bespokebots.models.tools.todoist import TodoistProject 

def test_close_task():
    #first, create a new task to close  
    content = "Close me"
    task = CreateTaskTool().run({"content": content})

    #now close it
    close_tool = CloseTaskTool()
    close_tool.run({"task_id": task['id']})

    #make sure it's closed
    closed_task = close_tool.todoist_client.get_task(task['id'])
    assert closed_task is not None
    assert closed_task.is_completed == True