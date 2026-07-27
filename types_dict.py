from enum import Enum
from typing import TypedDict


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class Task(TypedDict):
    id: int
    description: str
    status: TaskStatus
    createdAt: str
    updatedAt: str
