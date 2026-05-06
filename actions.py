import functions
from types_dict import Task, TaskID


def add_task(task_name: str) -> None:

    data: list[Task] = []

    FILE_PATH = functions.pegar_caminho_absoluto()

    if FILE_PATH.exists():
        data = functions.read_data()

    else:
        data = []

    date_time = functions.get_date_time()

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
        functions.clear_terminal()
        print(f"\033[31m\nA terefa {task_name} já existe!\n\033[m")

    else:
        data.append(new_task)  # type: ignore

        functions.inserir_nos_dados(data)

        functions.clear_terminal()
        print(f"Tarefa '{task_name}' adicionada com sucesso!\n")


def update_task(id: TaskID) -> None:
    _exist = functions.check_task_exists(id)

    if _exist:
        print(f"\nAtualizando a tarefa de ID = {id}")
        task = input("Insira a nova tarefa: ")

        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["description"] = task
                    d["updateAt"] = functions.get_date_time()
                    break

            functions.inserir_nos_dados(data)

            functions.clear_terminal()
            print("\n\033[32mTarefa atualizada com sucesso!\033[m\n")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def delete_task(id: TaskID) -> None:

    data = functions.read_data()

    if not data:
        print("\n\033[31mNão há nenhuma tarefa\033[m\n")
        return

    new_data = [d for d in data if d.get("id") != id]

    if len(new_data) != len(data):
        functions.inserir_nos_dados(new_data)
        print(f"\n\033[32mTarefa com ID {id} excluída com sucesso!\033[m\n")

    else:
        print(f"\n\033[31mO ID {id} não foi encontrado na base de dados.\033[m\n")


def mark_in_progress(id: TaskID) -> None:
    _exist = functions.check_task_exists(id)

    if _exist:
        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["status"] = "em processo"
                    break

            functions.inserir_nos_dados(data)

            print("\n\033[32mtarefa alterada para 'em processo'\033[m")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def mark_done(id: TaskID) -> None:
    _exist = functions.check_task_exists(id)

    if _exist:
        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["status"] = "Concluída"

            functions.inserir_nos_dados(data)
            functions.clear_terminal()
            print("\n\033[32mtarefa alterada para 'concluída'\033[m")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def list_all() -> None:
    data = functions.read_data()

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
    data = functions.read_data()

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
    data = functions.read_data()

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
    data = functions.read_data()

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
