from functions import (
    clear_terminal,
    existe_a_tarefa,
    get_date_time,
    inserir_nos_dados,
    pegar_caminho_absoluto,
    read_data,
    trata_input,
)
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

        inserir_nos_dados(data)

        clear_terminal()
        print(f"Tarefa '{task_name}' adicionada com sucesso!\n")


def update_task(id: str | int):
    _exists = False

    is_number = trata_input(id)  # verifica se é um número

    if is_number:
        id = int(id)
        _exists = existe_a_tarefa(id)  # verifica se a tarefa existe

        if _exists:
            print(f"\nAtualizando a tarefa de id = {id}")
            task = input("Insira a nova tarefa: ")

            data = read_data()

            for d in data:
                if d["id"] == id:
                    d["description"] = task
                    d["updateAt"] = get_date_time()
                    break

            inserir_nos_dados(data)

            clear_terminal()
            print("\n\033[32mTarefa atualizada com sucesso!\033[m\n")

        else:
            clear_terminal()
            print(f"\n\033[31mA tarefa com id: {id} não existe!\033[m\n")


def delete_task(id: int):
    # _exists = existe_a_tarefa(id)
    # is_number = trata_input(id)
    ...


def mark_in_progress(): ...


def mark_done(): ...


def list_all(): ...


def list_done(): ...


def list_todo(): ...


def list_in_progress(): ...


# update_task(2)
