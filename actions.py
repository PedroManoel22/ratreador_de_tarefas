from typing import TypeAlias

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

TaskID: TypeAlias = str | int


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
        "status": "Pendente",
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


def update_task(id: TaskID) -> None:
    _exists = False

    is_number = trata_input(id)  # verifica se é um número

    if is_number:
        id = int(id)
        _exists = existe_a_tarefa(id)  # verifica se a tarefa existe

        if _exists:
            print(f"\nAtualizando a tarefa de id = {id}")
            task = input("Insira a nova tarefa: ")

            data = read_data()

            if data:
                for d in data:
                    if d.get("id") == id:
                        d["description"] = task
                        d["updateAt"] = get_date_time()
                        break

                inserir_nos_dados(data)

                clear_terminal()
                print("\n\033[32mTarefa atualizada com sucesso!\033[m\n")

            else:
                print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def delete_task(id: TaskID) -> None:
    _exists = False

    is_number = trata_input(id)

    if is_number:
        id = int(id)
        _exists = existe_a_tarefa(id)

        if _exists:
            print(f"\nDeletando a tarefa de id = {id}")

            data = read_data()

            if data:
                for d in data:
                    if d.get("id") == id:
                        data.remove(d)
                        break

                inserir_nos_dados(data)

                print("\n\033[32mTarefa exluida com sucesso!\033[m\n")

            else:
                print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def mark_in_progress(id: TaskID) -> None:
    _exists = False

    is_number = trata_input(id)

    if is_number:
        id = int(id)
        _exists = existe_a_tarefa(id)

        if _exists:
            data = read_data()

            if data:
                for d in data:
                    if d.get("id") == id:
                        d["status"] = "em processo"
                        break

                inserir_nos_dados(data)

                print("\n\033[32mtarefa alterada para 'em processo'\033[m")

            else:
                print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def mark_done(id: TaskID) -> None:
    _exists = False

    is_number = trata_input(id)

    if is_number:
        id = int(id)
        _exists = existe_a_tarefa(id)

        if _exists:
            data = read_data()

            if data:
                for d in data:
                    if d.get("id") == id:
                        d["status"] = "Concluída"

                inserir_nos_dados(data)
                clear_terminal()
                print("\n\033[32mtarefa alterada para 'concluída'\033[m")

            else:
                print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def list_all() -> None:
    data = read_data()

    if data:
        for d in data:
            for k, v in d.items():
                print(f"{k}, {v}")

            print()
            print("-" * 50)
            print()

    else:
        print("\n\033[31mNão há nenhuma tarefa para ser listada!\n\033[m")


def list_done() -> None:
    data = read_data()

    if data:
        for d in data:
            if d.get("status") == "Concluída":
                for k, v in d.items():
                    print(f"{k}, {v}")
                print()
                print("-" * 50)
                print()

    else:
        print("\n\033[31mNão há tarefa concluída!\n\033[m")


def list_todo() -> None:
    data = read_data()

    if data:
        for d in data:
            if d.get("status") == "Pendente":
                for k, v in d.items():
                    print(f"{k}, {v}")
                print()
                print("-" * 50)
                print()

    else:
        print("\n\033[31mNão há nenhuma tarefa Pendente!\n\033[m")


def list_in_progress() -> None:
    data = read_data()

    if data:
        for d in data:
            if d.get("status") == "em processo":
                for k, v in d.items():
                    print(f"{k}, {v}")
                print()
                print("-" * 50)
                print()

    else:
        print("\n\033[31mNão há nenhuma tarefa Pendente!\n\033[m")


list_in_progress()
