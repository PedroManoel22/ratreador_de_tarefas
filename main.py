from functions import user_input, cabecalho, add_task

if __name__ == '__main__':
    action = user_input(cabecalho())
    
    if action == 1:
        task_name = input(f"Qual tarefa deseja adicionar? ").strip()
        add_task(task_name)