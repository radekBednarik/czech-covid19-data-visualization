import json
from typing import Any
from screeninfo import get_monitors


def save_json_data_to_file(filepath: str, data: Any) -> None:
    with open(filepath, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

    return None


def load_json_file(filepath: str) -> Any:
    with open(filepath, mode="r", encoding="utf-8") as file:
        data: Any = json.load(file)
    return data


def get_screen_res() -> Any:
    """Returns the first one monitor in case of multimonitor setup.

    Returns:
        Any: Monitor spec Class(x, y, width, height, name)
    """
    return get_monitors()[0]