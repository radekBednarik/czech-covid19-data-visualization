import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import pandas as pd
from covid19_api.src import api
from pandas import DataFrame

# TYPE ALIASES

# pylint: disable=unsubscriptable-object
Data = Optional[List[Dict[str, Any]]]
ResourceReturn = Optional[Dict[str, Union[str, Data]]]


def get(data: str = "infected") -> ResourceReturn:
    def _fetch(func):
        (check, raw_data) = func()
        if check:
            return raw_data
        return None

    if data == "infected":
        return _fetch(api.get_number_of_infected)

    if data == "tests":
        return _fetch(api.get_number_of_tests_done)

    if data == "all_numbers":
        return _fetch(api.get_all_numbers)

    if data == "basic_overview":
        return _fetch(api.get_basic_overview)

    if data == "cured":
        return _fetch(api.get_cured_overview)

    if data == "dead":
        return _fetch(api.get_deaths_overview)

    return None


def transform_for_histogram(data: Any) -> Any:
    df: DataFrame = DataFrame.from_records(data)
    df_m = df[df["pohlavi"] == "M"]["vek"].dropna()
    df_z = df[df["pohlavi"] == "Z"]["vek"].dropna()

    return {"men": df_m, "women": df_z}
