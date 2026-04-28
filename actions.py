from pathlib import Path
import json
from functions import get_date_time

def add_task(task_name: str):
    DIR_ROOT = Path(__file__).parent
    FILE_NAME = "data.json"
    FILE_PATH = DIR_ROOT / FILE_NAME

    data = []

    if FILE_PATH.exists():
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                # garante que data seja uma lista para podermos usar append
                if not isinstance(data, list):
                    data = []
        except (json.JSONDecodeError, ValueError):
            # Se o arquivo estiver corrompido ou vazio, começamos do zero
            data = []
    else:
        data = []
    
    date_time = get_date_time()

    
    new_task: dict[str, str | int] = {"id": len(data) + 1, "description": task_name, "status": "todo", "createAt": date_time , "updateAt": date_time } # type: ignore

    data.append(new_task) # type: ignore

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Tarefa '{task_name}' adicionada com sucesso!")
    