from __future__ import annotations

from typing import TYPE_CHECKING
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict
from todoist_api_python.models import Project, Task, Due


# The Todoist Model, Task:
# Task(
#     creator_id: "2671355",
#     created_at: "2019-12-11T22:36:50.000000Z",
#     assignee_id: "2671362",
#     assigner_id: "2671355",
#     comment_count: 10,
#     is_completed: False,
#     content: "Buy Milk",
#     description: "",
#     due: {
#         date: "2016-09-01",
#         is_recurring: false,
#         datetime: "2016-09-01T12:00:00.000000Z",
#         string: "tomorrow at 12",
#         timezone: "Europe/Moscow"
#     },
#     id: "2995104339",
#     labels: ["Food", "Shopping"],
#     order: 1,
#     priority: 1,
#     project_id: "2203306141",
#     section_id: "7025",
#     parent_id: "2995104589",
#     url: "https://todoist.com/showTask?id=2995104339"
# )

class TodoistTask(BaseModel):
    id: str = Field(..., title="Task ID", description="The ID of the task")

    project_id: str = Field(
        ...,
        title="Task Project ID",
        description="The ID of the project the task belongs to",
    )

    is_completed: bool = Field(
        ...,
        title="Task Completed",
        description="Whether the task is completed",
    )

    order: int = Field(
        ...,
        title="Task Order",
        description="The order of the task",
    )

    url: str = Field(
            ...,
            title="Task URL",
            description="The URL of the task",
        )
    
    creator_id: str = Field(
        ...,
        title="Task Creator ID",
        description="The ID of the user who created the task",
    )

    created_at: str = Field(
        ...,
        title="Task Created At",
        description="The date and time the task was created",
    )

    
    content: str = Field(
        title="Task Content",
        description="The content of the task, the content may contain markdown.",
        default=""
    )

    description: str = Field(
        title="Task Description",
        description="The description of the task.  If there is no description, this will be set to an empty string.",
        default=""
    )

    labels: List[str] = Field(
        title="Task Labels",
        description="The labels of the task",
        default=[]
    )

    
    priority: int = Field(
        title="Task Priority",
        description="The priority of the task from 1 (normal) to 4 (urgent), 1 is the default",
        default=1
    )

 
    comment_count: int = Field(
        title="Task Comment Count",
        description="The number of comments on the task, default is 0.",
        default=0
    )

    
    section_id: Optional[str] = Field(
        None,
        title="Task Section ID",
        description="The ID of the section the task's Project belongs to",
    )

    parent_id: Optional[str] = Field(
        None,
        title="Task Parent ID",
        description="The ID of the parent task, top-level tasks don't have a parent id.",
    )

    due: Optional[TodoistDue] = Field(
        None,
        title="Task Due",
        description="The due date of the task",
    )
    

    assignee_id: Optional[str] = Field(
        None,
        title="Task Assignee ID",
        description="The ID of the user who the task is assigned to",
    )

    assigner_id: Optional[str] = Field(
        None,
        title="Task Assigner ID",
        description="The ID of the user who assigned the task",
    )

    @classmethod
    def from_todoist(cls, todoist_task: Task) -> TodoistTask:
        return cls(
            id=todoist_task.id,
            project_id=todoist_task.project_id,
            section_id=todoist_task.section_id,
            content=todoist_task.content,
            description=todoist_task.description,
            is_completed=todoist_task.is_completed,
            labels=todoist_task.labels,
            order=todoist_task.order,
            priority=todoist_task.priority,
            url=todoist_task.url,
            comment_count=todoist_task.comment_count,
            creator_id=todoist_task.creator_id,
            created_at=todoist_task.created_at,
            parent_id=todoist_task.parent_id,
            due=TodoistDue.from_todoist(todoist_task.due) if todoist_task.due else None,
            assignee_id=todoist_task.assignee_id,
            assigner_id=todoist_task.assigner_id,
        )
    


class TodoistDue(BaseModel):

    string: str = Field(
        ...,
        title="Task Due String",
        description="Human defined date in arbitrary format.",
    )
    
    date: str = Field(
        ...,
        title="Task Due Date",
        description="Date in format YYYY-MM-DD corrected to user's timezone.",
    )

    is_recurring: bool = Field(
        ...,
        title="Task Due Is Recurring",
        description="Whether the task has a recurring due date.", 
    )

    datetime: Optional[str] = Field(
        None,
        title="Task Due Datetime",
        description="Date and time in RFC3339 format in UTC. Only set if the task has a specific time due",
    )  

    timezone: Optional[str] = Field(
        None,
        title="Task Due Timezone",
        description="Timezone of the due date. Only set if the task has a specific time due", 
    )

    @classmethod
    def from_todoist(cls, todoist_due: Due) -> TodoistDue:
        return cls(
            string=todoist_due.string,
            date=todoist_due.date,
            is_recurring=todoist_due.is_recurring,
            datetime=todoist_due.datetime,
            timezone=todoist_due.timezone,
        )
    
TodoistTask.update_forward_refs()