import json

from functions import clear_terminal, get_date_time, pegar_caminho_absoluto, read_data
from types_dict import Task


def add_task(task_name: str) -> None:

    data: list[Task] = []

    FILE_PATH = pegar_caminho_absoluto()

    if FILE_PATH.exists():
        data = read_data()

    else:
        data = []

    date_time = get_date_time()

    new_task: Task = {
        "id": len(data) + 1,
        "description": task_name,
        "status": "todo",
        "createdAt": date_time,
        "updateAt": date_time,
    }

    # Verificando se a tarefa que o usuário quer inserir já existe
    _exists = False

    for d in data:
        if task_name in d["description"]:
            _exists = True
            break

    if _exists:
        clear_terminal()
        print(f"\033[31m\nA terefa {task_name} já existe!\n\033[m")

    else:
        data.append(new_task)  # type: ignore

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        clear_terminal()
        print(f"Tarefa '{task_name}' adicionada com sucesso!\n")


def update_task(id: int):

    data = read_data()

    for d in data:
        if id == d["id"]:
            print(f"Id: {id} existe!")

        else:
            print(f"Id: {id} Não existe!")


def delete_task(): ...


def mark_in_progress(): ...


def mark_done(): ...


def list_all(): ...


def list_done(): ...


def list_todo(): ...


def list_in_progress(): ...
