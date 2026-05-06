import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, List

from types_dict import Task


def cabecalho(first_time: bool = False) -> int:
    ACTIONS: dict[int, str] = {
        1: "Adicionar tarefa",
        2: "Atualizar tarefa",
        3: "Excluir tarefa",
        4: "Marcar tarefa como 'em andamento",
        5: "Marcar tarefa como 'concluída'",
        6: "Listar todas as tarefas",
        7: "Listar todas as terefas que foram realizadas",
        8: "Listar todas as tarefas que não foram realizadas",
        9: "Listar todas as tarefas em andamento",
    }

    if first_time:
        print("\n---- Olá, bem vindo ao seu rastreador de tarefas! ----\n")

    for k, v in ACTIONS.items():
        print(f"{k} -> {v}")

    num_of_tasks = len(ACTIONS)

    return num_of_tasks


def user_input(num_of_tasks: int) -> int | None:
    while True:
        try:
            answer = int(input("\nO que deseja? "))

            if answer <= 0 or answer > num_of_tasks and answer != 999:
                print(
                    f"\n\033[33mPor favor insira um número entre 1 a {num_of_tasks}\033[m"
                )
                continue

            elif answer == 999:
                break

            return answer

        except (ValueError, KeyboardInterrupt):
            print("\n\033[31mPor favor coloque um número inteiro!\033[m")


def get_date_time():
    now = datetime.now()

    formatted_date = now.strftime("%d/%m/%Y - %H:%M:%S")

    return formatted_date


def clear_terminal():
    os.system("cls")


def get_clean_input(prompt: str):
    """Captura e limpa o input, garantindo que não seja vazio."""
    while True:
        value = input(prompt).strip()
        if value:
            return value


def read_data() -> List[Task]:

    file = pegar_caminho_absoluto()

    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, ValueError):
        # Se o arquivo estiver corrompido ou vazio, começamos do zero
        return []


def pegar_caminho_absoluto():
    # Pegando o caminho absoluto de "data.json"
    DIR_ROOT = Path(__file__).parent
    FILE_NAME = "data.json"
    FILE_PATH = DIR_ROOT / FILE_NAME

    return FILE_PATH


def existe_a_tarefa(id: int) -> bool:

    data = read_data()
    _exists = False

    for d in data:
        if id == d["id"]:
            _exists = True

    if _exists:
        return True

    else:
        clear_terminal()
        print(f"\n\033[31mA tarefa com id {id} não existe!\033[m")
        return False


def trata_input(id: Any) -> bool:
    try:
        int(id)
        return True

    except (ValueError, KeyboardInterrupt):
        print("\n\033[31mPor favor coloque um número inteiro\033[m\n")
        return False


def inserir_nos_dados(dados: list[Task] | str):
    FILE_PATH = pegar_caminho_absoluto()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def check_task_exists(task_id: str | int) -> bool:
    """Valida se o id é numérico e verfica a existência da tarefa."""

    is_numeric = trata_input(task_id)

    if not is_numeric:
        return False

    try:
        return existe_a_tarefa(int(task_id))

    except (ValueError, TypeError):
        return False
