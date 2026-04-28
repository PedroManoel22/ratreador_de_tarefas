
from datetime import datetime

def cabecalho() -> int:
    ACTIONS: dict[int, str] = {1:"Adicionar tarefa", 2:"Atualizar tarefa", 3:"Excluir tarefa", 4:"Marcar tarefa como 'em andamento",
            5:"Marcar tarefa como 'concluída'", 6:"Listar todas as tarefas", 7:"Listar todas as terefas que foram realizadas",
            8:"Listar todas as tarefas que não foram realizadas", 9:"Listar todas as tarefas em andamento"}


    print("\nOlá, bem vindo ao seu rastreador de tarefas!\n")

    for k, v in ACTIONS.items():
        print(f"{k} -> {v}")
    
    num_of_tasks = len(ACTIONS)

    return num_of_tasks
    
    

def user_input(num_of_tasks: int) -> int | None:
    while True:
        try:
            answer = int(input("\nO que deseja? "))

            if answer <=0 or answer > num_of_tasks and answer != 999:
                print(f"\n\033[33mPor favor insira um número entre 1 a {num_of_tasks}\033[m")
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
    