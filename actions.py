import functions
from types_dict import Task, TaskID


def add_task(task_name: str) -> None:
    """Adiciona uma nova tarefa ao arquivo de persistência JSON.

    Verifica a existência do arquivo de dados e carrega o estado atual.
    Se a tarefa com o mesmo nome já existir, a operação é abortada
    com um alerta ao usuário. Caso contrário, uma nova entrada é gerada
    com metadados de data e ID incremental.

    Args:
        task_name (str): O nome/descrição da tarefa a ser criada.

    Returns:
        None: A função realiza operações de I/O e exibe mensagens no terminal.

    Raises:
        OSError: Pode ocorrer se houver falha na permissão de escrita do arquivo."""

    data: list[Task] = []

    FILE_PATH = functions.get_absolute_path()

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
        "updatedAt": date_time,
    }

    # Verificando se a tarefa que o usuário quer inserir já existe
    _exists = functions.check_task_exists(new_task["id"])

    for d in data:
        if task_name in d["description"]:
            _exists = True
            break

    if _exists:
        functions.clear_terminal()
        print(f"\033[31m\nA terefa {task_name} já existe!\n\033[m")

    else:
        data.append(new_task)  # type: ignore

        functions.save_data(data)

        functions.clear_terminal()
        print(f"Tarefa '{task_name}' adicionada com sucesso!\n")


def update_task(id: TaskID) -> None:
    """Atualiza a descrição de uma tarefa existente no banco de dados.

    A função solicita uma nova descrição via input do usuário, localiza a
    tarefa pelo ID fornecido e atualiza tanto o conteúdo quanto o
    timestamp de modificação ('updatedAt').]
    Caso a tarefa não exista o usuário é informado com uma mensagem colorida
    na cor vermelha que tal tarefa não existe.

    Args:
        id (TaskID): O identificador único da tarefa a ser modificada.

    Returns:
        None: A função modifica os dados persistidos e gera saída no terminal.

    Note:
        Se o ID não for encontrado ou a base de dados estiver vazia,
        uma mensagem de erro amigável é exibida ao usuário."""

    _exist = functions.check_task_exists(id)

    if _exist:
        print(f"\nAtualizando a tarefa de ID = {id}")
        task = input("Insira a nova tarefa: ")

        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["description"] = task
                    d["updatedAt"] = functions.get_date_time()
                    break

            functions.save_data(data)

            functions.clear_terminal()
            print("\n\033[32mTarefa atualizada com sucesso!\033[m\n")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def delete_task(id: TaskID) -> None:
    """Deleta uma tarefa existente no banco de dados.

    A função solicita o ID da tarefa a ser excluída, localiza a
    tarefa pelo ID fornecido, e deleta tal tarefa.
    Caso a tarefa não exista o usuário é informado com uma mensagem colorida
    na cor vermelha que tal tarefa não existe.

    Args:
        id (TaskID): O identificador único da tarefa a ser excluída.

    Returns:
        None: A função modifica os dados persistidos e gera saída no terminal.

    Note:
        Se o ID não for encontrado ou a base de dados estiver vazia,
        uma mensagem de erro amigável é exibida ao usuário."""

    data = functions.read_data()

    if not data:
        print("\n\033[31mNão há nenhuma tarefa\033[m\n")
        return

    new_data = [d for d in data if d.get("id") != id]

    if len(new_data) != len(data):
        functions.save_data(new_data)
        print(f"\n\033[32mTarefa com ID {id} excluída com sucesso!\033[m\n")

    else:
        print(f"\n\033[31mO ID {id} não foi encontrado na base de dados.\033[m\n")


def mark_in_progress(id: TaskID) -> None:
    """Marca uma tarefa existente no banco de dados como "em andamento".

    A função solicita o ID da tarefa a ser marcada como "em andamento", localiza a
    tarefa pelo ID fornecido, e atualiza o status da tarefa.
    Caso a tarefa não exista o usuário é informado com uma mensagem colorida
    na cor vermelha que tal tarefa não existe.

    Args:
        id (TaskID): O identificador único da tarefa a ser marcada como "em andamento".

    Returns:
        None: A função modifica os dados persistidos e gera saída no terminal.

    Note:
        Se o ID não for encontrado ou a base de dados estiver vazia,
        uma mensagem de erro amigável é exibida ao usuário."""

    _exist = functions.check_task_exists(id)

    if _exist:
        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["status"] = "em processo"
                    break

            functions.save_data(data)

            print("\n\033[32mtarefa alterada para 'em processo'\033[m\n")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def mark_done(id: TaskID) -> None:
    """Marca uma tarefa existente no banco de dados como "concluída".

    A função solicita o ID da tarefa a ser marcada como "concluída", localiza a
    tarefa pelo ID fornecido, e atualiza o status da tarefa.
    Caso a tarefa não exista o usuário é informado com uma mensagem colorida
    na cor vermelha que tal tarefa não existe.

    Args:
        id (TaskID): O identificador único da tarefa a ser marcada como "concluída".

    Returns:
        None: A função modifica os dados persistidos e gera saída no terminal.

    Note:
        Se o ID não for encontrado ou a base de dados estiver vazia,
        uma mensagem de erro amigável é exibida ao usuário."""

    _exist = functions.check_task_exists(id)

    if _exist:
        data = functions.read_data()

        if data:
            for d in data:
                if d.get("id") == id:
                    d["status"] = "Concluída"

            functions.save_data(data)
            functions.clear_terminal()
            print("\n\033[32mtarefa alterada para 'concluída'\033[m\n")

        else:
            print("\n\033[31mNão há nenhuma tarefa\033[m\n")


def list_all() -> None:
    """Lista todas as tarefas armazenadas de forma estruturada no console.

    A função recupera a coleção de tarefas do arquivo de persistência e itera
    sobre cada registro, exibindo pares de chave-valor. Se a base de dados
    estiver vazia, notifica o usuário com uma mensagem de alerta.

    Returns:
        None: A saída é enviada diretamente para o stdout (terminal).

    Note:
        Utiliza sequências de escape ANSI para coloração de mensagens de erro.."""
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
    """Lista as tarefas marcada como "concluídas" armazenadas de forma estruturada no console.

    A função recupera a coleção de tarefas marcadas como "concluídas" do arquivo de persistência e itera
    sobre cada registro, exibindo pares de chave-valor. Se a base de dados não ter
    tarefas marcadas como "concluídas", notifica o usuário com uma mensagem de alerta.

    Returns:
        None: A saída é enviada diretamente para o stdout (terminal).

    Note:
        Utiliza sequências de escape ANSI para coloração de mensagens de erro.
    """

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
        print("\n\033[31mNão há tarefa concluída!\n\033[m\n")


def list_todo() -> None:
    """Lista as tarefas marcada como "pendente" armazenadas de forma estruturada no console.

    A função recupera a coleção de tarefas marcadas como "pendente" do arquivo de persistência e itera
    sobre cada registro, exibindo pares de chave-valor. Se a base de dados não ter
    tarefas marcadas como "pendente", notifica o usuário com uma mensagem de alerta.

    Returns:
        None: A saída é enviada diretamente para o stdout (terminal).

    Note:
        Utiliza sequências de escape ANSI para coloração de mensagens de erro.."""
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
    """Lista as tarefas marcada como "em processo" armazenadas de forma estruturada no console.

    A função recupera a coleção de tarefas marcadas como "em processo" do arquivo de persistência e itera
    sobre cada registro, exibindo pares de chave-valor. Se a base de dados não ter
    tarefas marcadas como "em processo", notifica o usuário com uma mensagem de alerta.

    Returns:
        None: A saída é enviada diretamente para o stdout (terminal).

    Note:
        Utiliza sequências de escape ANSI para coloração de mensagens de erro..
    """
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
