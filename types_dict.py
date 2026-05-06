from typing import TypeAlias, TypedDict


class Task(TypedDict):
    id: int
    description: str
    status: str
    createdAt: str
    updateAt: str


TaskID: TypeAlias = str | int
