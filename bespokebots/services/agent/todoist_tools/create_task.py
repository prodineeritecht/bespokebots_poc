from __future__ import annotations
from typing import Any, List, Optional, Type
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from bespokebots.services.agent.todoist_tools.base import TodoistBaseTool
from bespokebots.models.tools.todoist import (
    TodoistProject, 
    TodoistTask,
    TodoistDue
)

from todoist_api_python.models import Project



class CreateTaskSchema(BaseModel):
    
    content: str = Field(
        ...,
        title="Task Content",

        description="Task content, also used as a title so should be succinct. This value may contain markdown-formatted text and hyperlinks."
    )

    description: Optional[str] = Field(
        None,
        title="Task Description",
        description="This is where important information relative to the task may be added, information that would make the title too long. The description may contain markdown-formatted text and hyperlinks."
    ) 

    project_id: Optional[int] = Field(
        None,
        title="Project ID",
        description="The ID of the project the task belongs to. If not specified, the task will be created in the Inbox."
    )

    section_id: Optional[int] = Field(
        None,
        title="Section ID",
        description="The ID of the section the task belongs to. If not specified, the task will be created at the bottom of the project."
    )

    order: Optional[int] = Field(
        None,
        title="Order",
        description="The order of the task inside the project. The smallest value is 1."
    )

    labels: Optional[List[str]] = Field(
        None,
        title="Labels",
        description="The labels associated with the task. If not specified, the task will have no labels."
    )

    priority: Optional[int] = Field(
        None,
        title="Priority",
        description="The priority of the task from 1 (normal) to 4 (urgent), 1 is the default."
    )

    due_string: Optional[str] = Field(
        None,
        title="Due String",
        description="The human defined date string for when the task is due. If not set, the task will be created without a due date."
    )

    due_date: Optional[str] = Field(
        None,
        title="Due Date",
        description="The date when the task is due. If not set, the task will be created without a due date."
    )

    due_datetime: Optional[str] = Field(
        None,
        title="Due Datetime",
        description="The datetime when the task is due. If not set, the task will be created without a due date."
    )

    due_lang: Optional[str] = Field(
        None,
        title="Due Language",
        description="The language of the due_string. If not set, the language will be inferred from the content."
    )

    assignee: Optional[int] = Field(
        None,
        title="Assignee",
        description="The ID of the user to assign the task to. If not set, the task will be assigned to the current user."
    )

    parent_id: Optional[int] = Field(
        None,
        title="Parent ID",
        description="The ID of the parent task. this should be set to the task id of the parent project if the task being created is a subtask."
    )

class CreateTaskTool(TodoistBaseTool): 
    name: str = "create_task"
    description: str = """Use this tool when you need to create a task in Todoist for a client. The only required field, content, will be used as the task title. If no project_id is specified, the task will be created in the Inbox."""
    
    args_schema: Type[CreateTaskSchema] = CreateTaskSchema

    def _run(
        self, 
        content: str,
        description: Optional[str] = None,
        project_id: Optional[int] = None,
        section_id: Optional[int] = None,
        order: Optional[int] = None,
        labels: Optional[List[str]] = None,
        priority: Optional[int] = None,
        due_string: Optional[str] = None,
        due_date: Optional[str] = None,
        due_datetime: Optional[str] = None,
        due_lang: Optional[str] = None,
        assignee: Optional[int] = None,
        parent_id: Optional[int] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> dict:
        """Run the tool"""
        try:
            task = self.todoist_client.add_task(
                content=content,
                description=description,
                project_id=project_id,
                section_id=section_id,
                order=order,
                labels=labels,
                priority=priority,
                due_string=due_string,
                due_date=due_date,
                due_datetime=due_datetime,
                due_lang=due_lang,
                assignee=assignee,
                parent_id=parent_id
            )

            return TodoistTask.from_todoist(task).dict()
        except Exception as e:
            raise Exception(f"An error occurred when trying to create a task: {e}")
        
    async def _arun(self, *args: Any, **kwargs: Any) -> dict:
        raise NotImplementedError(f"The tool {self.name} does not support async yet.")