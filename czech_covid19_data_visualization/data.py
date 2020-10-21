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

    if data == "cured_men":
        return _fetch(api.get_cured_overview)

    return None


def make_bins(data: Any) -> Any:
    df: DataFrame = DataFrame.from_records(data)
    df_m = df[df["pohlavi"] == "M"]
    df_z = df[df["pohlavi"] == "Z"]
    bins = pd.IntervalIndex.from_tuples(
        [(0, 18), (19, 30), (31, 50), (51, 65), (66, 75), (76, 120)]
    )

    # and change types to be compatible with DASH serialization requirements :(
    bins_m = pd.cut(df_m["vek"], bins, precision=0, include_lowest=True).to_list()
    bins_z = pd.cut(df_z["vek"], bins, precision=0, include_lowest=True).to_list()

    return {"men": bins_m, "women": bins_z}


# if __name__ == "__main__":
#     import pandas as pd
#     from pandas import DataFrame

#     df: DataFrame = DataFrame.from_records(get(data="cured_individuals")["data"])
#     df_m = df[df["pohlavi"] == "M"]
#     df_z = df[df["pohlavi"] == "Z"]

#     bins = pd.IntervalIndex.from_tuples(
#         [(0, 18), (19, 30), (31, 50), (51, 65), (66, 75), (76, 120)]
#     )

#     bins_m = pd.cut(df_m["vek"], bins, precision=0, include_lowest=True)
#     bins_z = pd.cut(df_z["vek"], bins, precision=0, include_lowest=True)
#     print(bins_m)
#     print(bins_z)
