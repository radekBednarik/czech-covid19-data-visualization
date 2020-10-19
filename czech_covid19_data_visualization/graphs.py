from typing import Any, Dict, List

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots


def vertical_bar_and_line(data: List[Dict[str, Any]], graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data)

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df.iloc[:, 0], y=df.iloc[:, 1]), secondary_y=False)
    fig.add_trace(go.Scatter(x=df.iloc[:, 0], y=df.iloc[:, 2]), secondary_y=True)

    return html.Div(
        id=f"graphWrapper_{graph_number}",
        children=[dcc.Graph(id=f"barLineChart_{graph_number}", figure=fig)],
    )
