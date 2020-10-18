from typing import Any, Dict

import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots


def graph_vertical_bar(data: Dict[str, Any], graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data)

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df.iloc[:, 0], y=df.iloc[:, 1]), secondary_y=False)
    fig.add_trace(go.Scatter(x=df.iloc[:, 0], y=df.iloc[:, 2]), secondary_y=True)

    return dcc.Graph(id=f"barchart_{graph_number}", figure=fig)
