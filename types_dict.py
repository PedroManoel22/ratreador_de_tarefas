from typing import TypedDict


class Task(TypedDict):
    id: int
    description: str
    status: str
    createdAt: str
    updateAt: str
