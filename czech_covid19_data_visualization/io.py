import json
from typing import Any


def save_json_data_to_file(filepath: str, data: Any) -> None:
    with open(filepath, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def load_json_file(filepath: str) -> Any:
    with open(filepath, mode="r", encoding="utf-8") as file:
        data: Any = json.load(file)
    return data