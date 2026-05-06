import actions
import functions

if __name__ == "__main__":
    welcome = True
    while True:
        action = functions.user_input(functions.header(first_time=welcome))
        welcome = False

        match action:
            case 1:
                task_name = functions.get_clean_input("Qual tarefa deseja adicionar? ")
                actions.add_task(task_name)

            case 2:
                task_id = functions.get_clean_input(
                    "Insira o id da tarefa que deseja atualizar? "
                )

                actions.update_task(task_id)

            case 3:
                task_id = functions.get_clean_input(
                    "Qual o id da tarefa que deseja excluir? "
                )
                actions.delete_task(task_id)

            case 4:
                task_id = functions.get_clean_input(
                    "Insira o id da tarefa deseja marcar como 'em andamento'? "
                )
                actions.mark_in_progress(task_id)

            case 5:
                task_id = functions.get_clean_input(
                    "Qual o id da tarefa deseja marcar como 'concluída'?"
                )
                actions.mark_done(task_id)

            case 6:
                functions.clear_terminal()
                print("\nListando todas as tarefas...\n")
                actions.list_all()

            case 7:
                functions.clear_terminal()
                print("\nListando todas as terefas concluídas...\n")
                actions.list_done()

            case 8:
                functions.clear_terminal()
                print("\nListando todas as tarefas que não foram realizadas...\n")
                actions.list_todo()

            case 9:
                print("\nListando todas as tarefas que estão em andamento...\n")
                actions.list_in_progress()

            case _:
                ...

        if not action:
            break
