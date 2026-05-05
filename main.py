from actions import add_task, delete_task, list_all, update_task
from functions import cabecalho, get_clean_input, user_input

if __name__ == "__main__":
    welcome = True
    while True:
        action = user_input(cabecalho(first_time=welcome))
        welcome = False

        match action:
            case 1:
                task_name = get_clean_input("Qual tarefa deseja adicionar? ")
                add_task(task_name)

            case 2:
                task_id = get_clean_input(
                    "Insira o id da tarefa que deseja atualizar? "
                )

                update_task(task_id)

            case 3:
                task_id = get_clean_input("Qual o id da tarefa que deseja excluir? ")
                delete_task(task_id)

            # case 4:
            #     task_name = get_clean_input(
            #         "Qual tarefa deseja marcar como 'em andamento'? "
            #     )
            #     mark_in_progress(task_name)

            # case 5:
            #     task_name = get_clean_input(
            #         "Qual tarefa deseja marcar como 'concluída'?"
            #     )
            #     mark_done(task_name)

            case 6:
                print("\nListando todas as tarefas...\n")
                list_all()

            # case 7:
            #     print("\nListando todas as terfas concluídas...")
            #     list_done()

            # case 8:
            #     print("\nListando todas as tarefas que não foram realizadas...\n")
            #     list_todo()

            # case 9:
            #     print("\nListando todas as tarefas que estão em andamento...\n")
            #     list_in_progress()

            case _:
                ...

        if not action:
            break
