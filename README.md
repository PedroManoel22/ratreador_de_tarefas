# Task Tracker CLI 🚀

Uma aplicação robusta de linha de comando para gerenciamento de tarefas, desenvolvida em Python. Este projeto segue os requisitos do desafio [Task Tracker](https://roadmap.sh/projects/task-tracker) do Roadmap.sh, focando em persistência de dados, organização modular e boas práticas de desenvolvimento backend.

## 📌 Sobre o Projeto

O **Task Tracker** permite que o usuário gerencie sua lista de afazeres diretamente pelo terminal. Os dados são persistidos em um arquivo JSON, garantindo que as informações não sejam perdidas ao fechar a aplicação.

Este projeto demonstra competências em:
* Manipulação de sistemas de arquivos (I/O) com JSON.
* Lógica de programação avançada e filtragem de dados.
* Interface de usuário em terminal (CLI) com suporte a cores ANSI.

## 🛠️ Tecnologias e Conceitos Aplicados

* **Python 3.10+**: Uso de recursos modernos como `match/case` para controle de fluxo.
* **Type Hinting**: Código documentado com tipos para facilitar a manutenção e prevenir erros.
* **Persistência em JSON**: Armazenamento estruturado de dados.
* **Modularização**: Divisão clara de responsabilidades entre funções de sistema (`functions.py`) e lógica de negócio (`actions.py`).
* **PEP 8**: Código escrito seguindo os padrões oficiais de estilo da comunidade Python.

## 🚀 Funcionalidades

| Recurso | Descrição |
| :--- | :--- |
| **Adicionar** | Cria tarefas com IDs auto-incrementais únicos. |
| **Listagem Geral** | Visualização de todas as tarefas cadastradas na base de dados. |
| **Listagem Filtrada** | Filtros específicos para visualizar tarefas por status: *não realizada*, *em andamento* ou *concluída*. |
| **Gestão de Status** | Alteração rápida do estado das tarefas para 'em andamento' ou 'concluída'. |
| **Atualização** | Alteração dinâmica da descrição de tarefas existentes. |
| **Exclusão** | Remoção segura de itens da base de dados. |
| **Feedback Visual** | Interface colorida (Cores ANSI) para indicar sucessos e erros no terminal. |

## 💻 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SeuUsuario/task-tracker-python.git](https://github.com/SeuUsuario/task-tracker-python.git)
