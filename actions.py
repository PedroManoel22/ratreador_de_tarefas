from pathlib import Path
import json
from typing import List, TypedDict
from functions import get_date_time, clear_terminal

# tipagem 
class Task(TypedDict):
    id: int
    description: str
    status: str
    createAt: str  
    updateAt: str


def add_task(task_name: str) -> None:
    DIR_ROOT = Path(__file__).parent
    FILE_NAME = "data.json"
    FILE_PATH = DIR_ROOT / FILE_NAME

    data: List[Task] = []

    if FILE_PATH.exists():
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

        except (json.JSONDecodeError, ValueError):
            # Se o arquivo estiver corrompido ou vazio, começamos do zero
            data = []
    else:
        data = []
    
    date_time = get_date_time()

    
    new_task: Task = {"id": len(data) + 1, "description": task_name, "status": "todo", "createAt": date_time , "updateAt": date_time }

    # Verificando se a tarefa que o usuário quer inserir já existe
    _exists = False

    for d in data:
        if task_name in d['description']:
            _exists = True
            break
    
    if _exists:
        clear_terminal()
        print(f"\033[31m\nA terefa {task_name} já existe!\n\033[m")
    
    else:
        data.append(new_task) # type: ignore

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        clear_terminal() 
        print(f"Tarefa '{task_name}' adicionada com sucesso!\n")


def update_task():...


def delete_task():...


def mark_in_progress():...


def mark_done():...


def list_all():...


def list_done():...


def list_todo():...


def list_in_progress():...