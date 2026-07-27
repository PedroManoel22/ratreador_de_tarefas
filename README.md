# Task Tracker CLI 🚀

Uma aplicação de linha de comando robusta, leve e profissional para gerenciamento de tarefas, desenvolvida em Python. Este projeto segue as especificações do desafio [Task Tracker](https://roadmap.sh/projects/task-tracker) do Roadmap.sh, focando em persistência de dados, arquitetura modular, interfaces CLI modernas e boas práticas de desenvolvimento backend.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Sobre o Projeto

O **Task Tracker CLI** permite que o usuário gerencie sua lista de afazeres de forma rápida e automatizável diretamente pelo terminal, utilizando subcomandos e flags. Os dados são persistidos localmente em um arquivo `JSON`, garantindo a integridade e manutenção das informações entre as execuções.

Este projeto demonstra competências técnicas essenciais para desenvolvedores backend:

- **Interface CLI Profissional:** Construção de parser de argumentos e subcomandos com a biblioteca padrão (`argparse`).
- **Manipulação I/O com JSON:** Leitura, escrita e validação de dados estruturados em arquivo local.
- **Tipagem Estática e Design Pattern:** Organização de tipos estruturados com `TypedDict`, Type Hints explícitos e separação de camadas (_Separation of Concerns_).
- **Boas Práticas de Código:** Garantia de compatibilidade com PEP 8, padronização via linter **Ruff** e tratamento de fusos horários UTC (`timezone-aware`).

---

## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3.10+**: Controle de fluxo moderno usando `match/case` para roteamento de subcomandos.
- **Standard Library Apenas**: Nenhuma biblioteca externa (`pip install`) é necessária para executar o projeto (`argparse`, `json`, `datetime`, `pathlib`).
- **Type Hinting & Static Typing**: Tipagem rigorosa nos parâmetros e retornos das funções.
- **Modularização**: Divisão estratégica das responsabilidades entre a CLI (`main.py`), regras de negócio (`actions.py`), funções de suporte (`functions.py`) e tipagens (`types_dict.py`).

---

## 🚀 Funcionalidades

| Recurso                 | Comando CLI              | Descrição                                                             |
| :---------------------- | :----------------------- | :-------------------------------------------------------------------- |
| **Adicionar**           | `add`                    | Cria tarefas com IDs únicos e carimbos de data/hora (UTC).            |
| **Listar Tudo**         | `list`                   | Exibe todas as tarefas cadastradas na base de dados.                  |
| **Listar Filtrado**     | `list --status <STATUS>` | Filtra tarefas por estado (`all`, `done`, `todo`, `in-progress`).     |
| **Atualizar Descrição** | `update`                 | Altera a descrição de uma tarefa pelo ID.                             |
| **Marcar Em Andamento** | `mark-in-progress`       | Altera o status da tarefa para `em andamento`.                        |
| **Marcar Concluída**    | `mark-done`              | Altera o status da tarefa para `concluída`.                           |
| **Excluir**             | `delete`                 | Remove permanentemente uma tarefa do arquivo JSON.                    |
| **Feedback Visual**     | -                        | Mensagens formatadas e coloridas (ANSI) indicando sucessos ou falhas. |

---

A aplicação foi desenhada como uma **CLI moderna e determinística**. Isso significa que você executa o comando completo diretamente no terminal sem a necessidade de menus interativos, facilitando a automação e integração com scripts Bash.

---

## 💻 Como Executar e Utilizar

### 0. Clonar o Repositório

```bash
git clone https://github.com/PedroManoel22/ratreador_de_tarefas.git
cd ratreador_de_tarefas
```

### 🔍 1. Consultando a Ajuda (`--help`)

Para visualizar todos os subcomandos e opções suportadas pela aplicação, utilize a flag de ajuda nativa:

```bash
python3 main.py --help
```

### 🔍 2. Adicionando Tarefas (`add`)

Cria tarefas com IDs únicos e carimbos de data/hora (UTC).

```bash
python3 main.py add "Estudar estrutura de dados em Python"
```

### 🔍 3. Listando Tarefas (`list`)

Exibe todas as tarefas cadastradas na base de dados.

```bash
python3 main.py list
```

### 🔍 3.1 Listando Tarefas por estado (`list`)

Filtra tarefas por estado (`all`, `done`, `todo`, `in-progress`).

```bash
python3 main.py list --status done
```

### 🔍 4 Atualizando a descrição (`update`)

Altera a descrição de uma tarefa pelo ID.

```bash
python3 main.py update 1 "Estudar estrutura de dados e algoritimos em Python"
```

### 🔍 5 Atualizando o status de uma tarefa (`mark-in-progress`)

Altera o status da tarefa para `em andamento`.

```bash
python3 main.py mark-in-progress 1
```

### 🔍 6 Atualizando o status de uma tarefa (`mark-done`)

Altera o status da tarefa para `concluída`.

```bash
python3 main.py mark-done 1
```

### 🔍 7 Removendo uma Tarefa (`delete`)

Remove permanentemente uma tarefa do arquivo JSON.

```bash
python3 main.py delete 2
```
