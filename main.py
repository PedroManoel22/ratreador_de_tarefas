from functions import user_input, cabecalho
from actions import add_task

def get_clean_input(prompt: str):
    """Captura e limpa o input, garantindo que não seja vazio."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Entrada inválida. Por favor, digite algum conteúdo.")


if __name__ == '__main__':
    welcome = True
    while True:
        action = user_input(cabecalho(first_time=welcome))
        welcome = False
     
        if action == 1:
            task_name = get_clean_input("Qual tarefa deseja adicionar? ")

            add_task(task_name)
        
        elif action is None:
            break
