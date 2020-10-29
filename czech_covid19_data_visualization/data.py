import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import pandas as pd
from covid19_api.src import api
from pandas import DataFrame, Series

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

    if data == "infected_individuals":
        return _fetch(api.get_infected_overview)

    return None


def get_all_data() -> Any:

    print(
        "Fetching all data via one big API call - this saves API calls to the data server and \
    \nspeeds up loading graphs of big data sets significantly. \
    \nHowever, to get new data, you must restart the the app, not just refresh the browser."
    )
    returned_data_dict: Dict[str, Any] = {}

    list_to_get: List[str] = [
        "infected",
        "tests",
        "all_numbers",
        "basic_overview",
        "cured",
        "dead",
        "infected_individuals",
    ]

    for each in list_to_get:
        returned_data_dict[each] = get(data=each)

    return returned_data_dict


def transform_for_histogram(data: Any) -> Any:
    df: DataFrame = DataFrame.from_records(data)
    df_m = df[df["pohlavi"] == "M"]["vek"].dropna()
    df_z = df[df["pohlavi"] == "Z"]["vek"].dropna()

    return {"men": df_m, "women": df_z}


def transform_for_index(
    data_one: Dict[str, Optional[Dict[str, Any]]],
    data_two: Dict[str, Optional[Dict[str, Any]]],
) -> Any:
    data_one_key: str = list(data_one.keys())[0]
    data_two_key: str = list(data_two.keys())[0]

    if data_one[data_one_key] is not None and data_two[data_two_key] is not None:

        df_one: DataFrame = DataFrame.from_dict(data_one[data_one_key]["data"])
        df_two: DataFrame = DataFrame.from_dict(data_two[data_two_key]["data"])

        df_one = DataFrame(df_one[data_one_key]).set_index(df_one["datum"])
        df_two = DataFrame(df_two[data_two_key]).set_index(df_two["datum"])

        final: Series = Series(
            df_one[data_one_key].div(df_two[data_two_key]), name="two_timeseries_index"
        ).dropna()
        final_trend: Series = final.rolling(7).mean()

        return (final, final_trend)
    return None


# if __name__ == "__main__":
#     result: Any = transform_for_index(
#         {"prirustkovy_pocet_nakazenych": get(data="infected")},
#         {"prirustkovy_pocet_testu": get(data="tests")},
#     )
