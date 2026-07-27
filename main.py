import argparse

import actions
from types_dict import TaskStatus


def build_parser() -> argparse.ArgumentParser:
    """Configura o parser de argumentos CLI."""
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="Gerenciador de tarefas via linha de comando (CLI)",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Comandos disponíveis"
    )

    # Comando: add
    add_parser = subparsers.add_parser("add", help="Adiciona uma nova tarefa")
    add_parser.add_argument("description", type=str, help="Descrição da tarefa")

    # Comando: update
    update_parser = subparsers.add_parser(
        "update", help="Atualiza a descrição de uma tarefa"
    )
    update_parser.add_argument("id", type=int, help="ID da tarefa")
    update_parser.add_argument("description", type=str, help="Nova descrição da tarefa")

    # Comando: delete
    delete_parser = subparsers.add_parser("delete", help="Remove uma tarefa pelo ID")
    delete_parser.add_argument("id", type=int, help="ID da tarefa")

    # Comando: mark-in-progress
    mark_prog_parser = subparsers.add_parser(
        "mark-in-progress", help="Marca a tarefa como 'em andamento'"
    )
    mark_prog_parser.add_argument("id", type=int, help="ID da tarefa")

    # Comando: mark-done
    mark_done_parser = subparsers.add_parser(
        "mark-done", help="Marca a tarefa como 'concluída'"
    )
    mark_done_parser.add_argument("id", type=int, help="ID da tarefa")

    # Comando: list
    list_parser = subparsers.add_parser("list", help="Lista as tarefas cadastradas")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["all", "done", "todo", "in-progress"],
        default="all",
        help="Filtro opcional pelo status da tarefa (padrão: all)",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    match args.command:
        case "add":
            actions.add_task(args.description)
        case "update":
            actions.update_task(args.id, args.description)
        case "delete":
            actions.delete_task(args.id)
        case "mark-in-progress":
            actions.update_status(args.id, TaskStatus.IN_PROGRESS)
        case "mark-done":
            actions.update_status(args.id, TaskStatus.DONE)
        case "list":
            actions.list_tasks(args.status)


if __name__ == "__main__":
    main()
