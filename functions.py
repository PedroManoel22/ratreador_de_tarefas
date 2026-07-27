import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from types_dict import Task

DATA_FILE = Path("tasks.json")


def get_absolute_path() -> Path:
    """Retorna o caminho absoluto do arquivo de dados JSON."""
    return DATA_FILE.resolve()


def get_date_time() -> str:
    """Retorna o timestamp atual formatado em padrão ISO/legível."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def read_data() -> list[Task]:
    """Carrega as tarefas armazenadas no arquivo JSON."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_data(data: list[Task]) -> None:
    """Persiste a lista de tarefas no arquivo JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"\033[31mErro ao salvar dados no arquivo: {e}\033[m", file=sys.stderr)


def generate_next_id(data: list[Task]) -> int:
    """Gera um ID único incremental seguro."""
    if not data:
        return 1
    return max(task["id"] for task in data) + 1
