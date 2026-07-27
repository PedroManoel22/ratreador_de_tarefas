import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from types_dict import Task


def header(first_time: bool = False) -> int:
    """Exibe o menu de opções do rastreador de tarefas e retorna o total de ações.

    A função renderiza uma saudação opcional (caso seja a primeira execução)
    e itera sobre um dicionário de ações disponíveis, numerando-as para o usuário.
    É utilizada como o ponto de entrada visual do loop principal da aplicação.

    Args:
        first_time (bool, optional): Se True, exibe uma mensagem de boas-vindas.
            O padrão é False.

    Returns:
        int: A quantidade total de opções disponíveis no menu (usado para validação de input)."""

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
    """Captura e valida a escolha do usuário no menu principal.

    A função executa um loop contínuo solicitando um número inteiro.
    Valida se a entrada está dentro do intervalo permitido pelas ações
    disponíveis ou se corresponde ao código de saída (999).

    Args:
        num_of_tasks (int): O limite superior de opções válidas no menu.

    Returns:
        int | None: Retorna o número da opção escolhida ou o código 999
            para encerrar o programa.

    Raises:
        ValueError: Capturado internamente caso o usuário insira caracteres não numéricos.
        KeyboardInterrupt: Capturado internamente para evitar o fechamento abrupto via Ctrl+C."""

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
    """Gera um carimbo de data e hora atual formatado.

    Recupera o instante exato do sistema e o converte em uma string
    legível seguindo o padrão brasileiro (DD/MM/AAAA - HH:MM:SS).

    Returns:
        str: Data e hora atuais formatadas (ex: "06/05/2026 - 17:15:30")."""

    now = datetime.now(timezone.utc)

    formatted_date = now.strftime("%d/%m/%Y - %H:%M:%S")

    return formatted_date


def clear_terminal():
    """
    Limpa o console do sistema operacional.

    Executa um comando de sistema para remover todo o texto visível no terminal,
    proporcionando uma interface mais limpa para o usuário.

    Returns:
        None: A função executa uma chamada de sistema e não retorna valores.

    Note:
        Atualmente implementada especificamente para ambientes Windows ('cls').
    """
    """Limpa o console do sistema operacional."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


def get_clean_input(prompt: str):
    """Captura e limpa o input, garantindo que não seja vazio."""
    while True:
        value = input(prompt).strip()
        if value:
            return value


def read_data() -> list[Task]:
    """Lê e decodifica o arquivo JSON de tarefas.

    Tenta abrir o arquivo de persistência utilizando codificação UTF-8.
    Caso o arquivo esteja corrompido ou não siga o formato JSON esperado,
    a função trata a exceção e retorna uma lista vazia para garantir a
    continuidade da execução.

    Returns:
        List[Task]: Uma lista de dicionários representando as tarefas.

    Raises:
        json.JSONDecodeError: Capturado se o arquivo não for um JSON válido."""

    file = get_absolute_path()

    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, ValueError):
        # Se o arquivo estiver corrompido ou vazio, começamos do zero
        return []


def get_absolute_path():
    """Resolve o caminho absoluto para o arquivo de dados 'data.json'.

    Utiliza a biblioteca pathlib para localizar o diretório onde o script
    está sendo executado e construir o caminho para o banco de dados JSON,
    garantindo que o arquivo seja encontrado independente de onde o script
    for chamado no sistema.

    Returns:
        Path: Objeto Path contendo o caminho absoluto do arquivo de dados."""

    DIR_ROOT = Path(__file__).parent
    FILE_NAME = "data.json"
    FILE_PATH = DIR_ROOT / FILE_NAME

    return FILE_PATH


def task_exists(id: int) -> bool:
    """Verifica a presença de uma tarefa específica na base de dados.

    Args:
        id (int): O identificador único da tarefa.

    Returns:
        bool: True se o ID for encontrado, False caso contrário (exibindo
            um alerta no terminal)."""

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


def validate_input(id: Any) -> bool:
    """Valida se uma entrada pode ser convertida para um número inteiro.

    Esta função atua como um 'guardião' de tipo, tentando realizar a
    conversão de uma entrada genérica. É fundamental para prevenir que
    caracteres inválidos quebrem a lógica de busca por ID.

    Args:
        id (Any): O valor a ser testado para conversão numérica.

    Returns:
        bool: True se a conversão for bem-sucedida, False caso ocorra
            erro de valor ou interrupção de teclado."""

    try:
        int(id)
        return True

    except (ValueError, KeyboardInterrupt):
        print("\n\033[31mPor favor coloque um número inteiro\033[m\n")
        return False


def save_data(dados: list[Task] | str):
    """Persiste o estado atual das tarefas no arquivo JSON.

    Abre o arquivo de dados em modo de escrita, utilizando indentação
    para garantir que o arquivo permaneça legível por humanos e
    assegurando a compatibilidade de caracteres especiais (UTF-8).

    Args:
        dados (list[Task] | str): A coleção de tarefas ou string a ser salva."""
    FILE_PATH = get_absolute_path()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def check_task_exists(task_id: str | int) -> bool:
    """Orquestra a validação completa de existência de uma tarefa.

    Realiza uma verificação em duas etapas: primeiro valida a integridade
    numérica do ID e, em seguida, consulta a base de dados para confirmar
    se o registro existe.

    Args:
        task_id (str | int): O identificador fornecido pelo usuário.

    Returns:
        bool: True se o ID for válido e a tarefa existir na base."""

    is_numeric = validate_input(task_id)

    if not is_numeric:
        return False

    try:
        return task_exists(int(task_id))

    except (ValueError, TypeError):
        return False
