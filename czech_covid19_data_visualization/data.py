import json
from typing import Optional

import pandas as pd
from covid19_api.src import api
from pandas import DataFrame


# pylint: disable=unsubscriptable-object
def number_of_infected() -> Optional[DataFrame]:
    (check, raw_data) = api.get_number_of_infected()
    if check:
        data_str: str = json.dumps(raw_data["data"])
        df: DataFrame = pd.read_json(data_str)
        return df
    return None


if __name__ == "__main__":
    number_of_infected()
