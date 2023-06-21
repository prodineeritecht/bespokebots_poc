from __future__ import annotations

from typing import TYPE_CHECKING
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from todoist_api_python.models import Project, Section
from bespokebots.models.tools.todoist.task import (TodoistTask, TodoistDue)


class TodoistProject(BaseModel):
    """Data class representing a Todoist project summary"""

    id: int = Field(..., title="Project ID", description="The ID of the project")

    name: str = Field(..., title="Project Name", description="The name of the project")

    color: str = Field(
        ..., title="Project Color", description="The color of the project"
    )

    is_inbox_project: bool = Field(
        ...,
        title="Project Inbox",
        description="Whether the project is the inbox project",
    )

    is_team_inbox_: bool = Field(
        ...,
        title="Project Inbox",
        description="Whether the project is the inbox project",
    )

    is_favorite: int = Field(
        ..., title="Project Favorite", description="Whether the project is a favorite"
    )

    comment_count: int = Field(
        ...,
        title="Project Comment Count",
        description="The comment count of the project",
    )

    url: str = Field(..., title="Project URL", description="The URL of the project")

    # open_item_count: int = Field(
    #     ...,
    #     title="Project Open Item Count",
    #     description="The number of open items in the project",
    # )

    # There doesn't seem to be a simple way to get the number of completed items in a project,
    # we would have to keep track of the number of completed items ourselves.  Not a right now thing.
    # completed_item_count: int = Field(
    #     ...,
    #     title="Project Completed Item Count",
    #     description="The number of completed items in the project",
    # )
    tasks: List[TodoistTask] = Field(
        title="Project Tasks",
        description="List of the active tasks in the project",
        default=[]
    )

    sync_id: Optional[int] = Field(
        None, title="Project Sync ID", description="The sync ID of the project"
    )
    user_id: Optional[int] = Field(
        None, title="Project User ID", description="The user ID of the project"
    )
    parent_id: Optional[int] = Field(
        None, title="Project Parent ID", description="The parent ID of the project"
    )
    
    def num_open_tasks(self):
        return len(self.tasks)
    
    
    @classmethod
    def from_todoist(cls, project: Project) -> TodoistProject:
        return cls(
            id=project.id,
            name=project.name,
            color=project.color,
            is_inbox_project=project.is_inbox_project,
            is_team_inbox_=project.is_team_inbox,
            is_favorite=project.is_favorite,
            comment_count=project.comment_count,
            url=project.url,
            parent_id=project.parent_id,
        )
    
    @classmethod    
    def find_project_by_name(cls, projects: List[TodoistProject], name: str) -> Optional[TodoistProject]:
        return next((p for p in projects if p.name == "Office Decluttering"), None)
    
    @classmethod
    def project_list_to_dict(cls, projects: List[TodoistProject]) -> Dict[str, List[Dict[str, Any]]]:
        project_dicts = []
        for project in projects:
            project_dict = project.dict()
            project_dict["tasks"] = [task.dict() for task in project.tasks] if project.tasks else []
            project_dicts.append(project_dict)  

        return {"projects": project_dicts}


class TodoistSection(BaseModel):
    """Data model class representing a Todoist Section resource"""

    id: str = Field(..., title="Section ID", description="The ID of the section")
    name: str = Field(..., title="Section Name", description="The name of the section")
    project_id: str = Field(
        ..., title="Project ID", description="The project ID of the project which the section belongs to"
    )
    order: int = Field(..., title="Section Order", description="The order of the section")

    @classmethod
    def from_todoist(cls, section: Section) -> TodoistSection:
        return cls(
            id=section.id,
            name=section.name,
            project_id=section.project_id,
            order=section.order,
        )
