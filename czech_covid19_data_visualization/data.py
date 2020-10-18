import json
from typing import Any, Dict, Optional

import pandas as pd
from covid19_api.src import api
from pandas import DataFrame


# pylint: disable=unsubscriptable-object
def number_of_infected() -> Optional[Dict[str, Any]]:
    (check, raw_data) = api.get_number_of_infected()
    if check:
        return raw_data["data"]
    return None


if __name__ == "__main__":
    number_of_infected()
