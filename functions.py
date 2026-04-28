from pathlib import Path
import json

def cabecalho() -> int:
    ACTIONS: dict[int, str] = {1:"Adicionar tarefa", 2:"Atualizar tarefa", 3:"Excluir tarefa", 4:"Marcar tarefa como 'em andamento",
            5:"Marcar tarefa como 'concluída'", 6:"Listar todas as tarefas", 7:"Listar todas as terefas que foram realizadas",
            8:"Listar todas as tarefas que não foram realizadas", 9:"Listar todas as tarefas em andamento"}


    print("\nOlá, bem vindo ao seu rastreador de tarefas!\n")

    for k, v in ACTIONS.items():
        print(f"{k} -> {v}")
    
    num_of_tasks = len(ACTIONS)

    return num_of_tasks
    
    

def user_input(num_of_tasks: int) -> int:
    while True:
        try:
            answer = int(input("\nO que deseja? "))

            if answer <=0 or answer > num_of_tasks:
                print(f"\n\033[33mPor favor insira um número entre 1 a {num_of_tasks}\033[m")
                continue
            break
        
        except (ValueError, KeyboardInterrupt):
            print("\n\033[31mPor favor coloque um número inteiro!\033[m")
        
    return answer


def add_task(task_name: str):
    DIR_ROOT = Path(__file__).parent
    FILE_NAME = "data.json"
    FILE_PATH = DIR_ROOT / FILE_NAME

    if FILE_PATH.exists():
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                # garante que data seja uma lista para podermos usar append
                if not isinstance(data, list):
                    data = []
        except (json.JSONDecodeError, ValueError):
            # Se o arquivo estiver corrompido ou cazio, começamos do zero
            data = []
    else:
        data = []
    
 
    