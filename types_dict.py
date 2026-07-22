from typing import TypeAlias, TypedDict


class Task(TypedDict):
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str


TaskID: TypeAlias = str | int
