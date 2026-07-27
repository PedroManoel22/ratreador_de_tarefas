import functions
from types_dict import Task, TaskStatus


def add_task(description: str) -> None:
    """Adiciona uma nova tarefa à base de dados."""
    description = description.strip()
    if not description:
        print("\033[31mA descrição da tarefa não pode ser vazia!\033[m")
        return

    data = functions.read_data()

    if any(t["description"].lower() == description.lower() for t in data):
        print(f"\033[31mA tarefa '{description}' já existe!\033[m")
        return

    now = functions.get_date_time()
    new_task: Task = {
        "id": functions.generate_next_id(data),
        "description": description,
        "status": TaskStatus.TODO,
        "createdAt": now,
        "updatedAt": now,
    }

    data.append(new_task)
    functions.save_data(data)
    print(
        f"\033[32mTarefa '{description}' adicionada com sucesso! (ID: {new_task['id']})\033[m"
    )


def update_task(task_id: int, new_description: str) -> None:
    """Atualiza a descrição de uma tarefa existente pelo seu ID."""
    new_description = new_description.strip()
    if not new_description:
        print("\033[31mA nova descrição não pode ser vazia!\033[m")
        return

    data = functions.read_data()
    for task in data:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = functions.get_date_time()
            functions.save_data(data)
            print(f"\033[32mTarefa ID {task_id} atualizada com sucesso!\033[m")
            return

    print(f"\033[31mTarefa com ID {task_id} não encontrada.\033[m")


def delete_task(task_id: int) -> None:
    """Remove uma tarefa da base de dados pelo seu ID."""
    data = functions.read_data()
    filtered_data = [t for t in data if t["id"] != task_id]

    if len(filtered_data) == len(data):
        print(f"\033[31mTarefa com ID {task_id} não encontrada.\033[m")
        return

    functions.save_data(filtered_data)
    print(f"\033[32mTarefa com ID {task_id} excluída com sucesso!\033[m")


def update_status(task_id: int, status: TaskStatus) -> None:
    """Atualiza o status de uma tarefa pelo seu ID."""
    data = functions.read_data()
    for task in data:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = functions.get_date_time()
            functions.save_data(data)
            print(
                f"\033[32mStatus da tarefa ID {task_id} alterado para '{status.value}'!\033[m"
            )
            return

    print(f"\033[31mTarefa com ID {task_id} não encontrada.\033[m")


def list_tasks(status_filter: str | None = "all") -> None:
    """Lista tarefas cadastradas com formatação e filtro opcional de status."""
    data = functions.read_data()
    if not data:
        print("\033[31mNenhuma tarefa cadastrada na base de dados.\033[m")
        return

    if status_filter and status_filter != "all":
        data = [t for t in data if t["status"] == status_filter]

    if not data:
        print(
            f"\033[33mNenhuma tarefa encontrada com o status '{status_filter}'.\033[m"
        )
        return

    print("\n" + "=" * 60)
    for task in data:
        status_val = (
            task["status"].value
            if isinstance(task["status"], TaskStatus)
            else task["status"]
        )
        print(f"ID: {task['id']} | [{status_val.upper()}] - {task['description']}")
        print(f"Criada em: {task['createdAt']} | Atualizada em: {task['updatedAt']}")
        print("-" * 60)
    print()
