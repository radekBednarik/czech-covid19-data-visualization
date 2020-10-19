import json
from typing import Any, Callable, Dict, Optional, List, Tuple, Union

from covid19_api.src import api
from pandas import DataFrame

# TYPE ALIASES

# pylint: disable=unsubscriptable-object
Data = Optional[List[Dict[str, Any]]]


def get(data: str = "infected") -> Data:
    def _fetch(func):
        (check, raw_data) = func()
        if check:
            return raw_data["data"]
        return None

    if data == "infected":
        return _fetch(api.get_number_of_infected)

    if data == "tests":
        return _fetch(api.get_number_of_tests_done)

    if data == "all_numbers":
        return _fetch(api.get_all_numbers)

    return None
