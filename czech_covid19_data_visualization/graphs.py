from typing import Any, Dict

import dash_core_components as dcc
import pandas as pd
from pandas import DataFrame
import plotly.graph_objects as go


def graph_vertical_bar(data: Dict[str, Any], graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data)

    return dcc.Graph(
        id=f"barchart_{graph_number}",
        figure=go.Figure(
            data=[
                go.Bar(x=df.iloc[:, 0], y=df.iloc[:, 1]),
                go.Scatter(x=df.iloc[:, 0], y=df.iloc[:, 2]),
            ]
        ),
    )
