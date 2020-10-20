from typing import Any, Dict, List, Tuple, Union, Optional

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots

# pylint: disable=unsubscriptable-object
Data = Dict[str, Union[str, List[Dict[str, Any]]]]


def vertical_bar_and_line_2inputs(data: Data, graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data["data"])
    labels: List[str] = df.columns

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(name=labels[1], x=df.iloc[:, 0], y=df.iloc[:, 1]), secondary_y=False
    )
    fig.add_trace(
        go.Scatter(name=labels[2], x=df.iloc[:, 0], y=df.iloc[:, 2]), secondary_y=True
    )

    return html.Div(
        id=f"graphWrapper_{graph_number}",
        children=[dcc.Graph(id=f"barLineChart_{graph_number}", figure=fig)],
    )


def line_3inputs(data: Data, graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data["data"])
    labels: List[str] = df.columns

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(name=labels[1], x=df.iloc[:, 0], y=df.iloc[:, 1]), secondary_y=False
    )
    fig.add_trace(
        go.Scatter(name=labels[2], x=df.iloc[:, 0], y=df.iloc[:, 2]), secondary_y=False
    )
    fig.add_trace(
        go.Scatter(name=labels[3], x=df.iloc[:, 0], y=df.iloc[:, 3]), secondary_y=True
    )

    return html.Div(
        id=f"graphWrapper_{graph_number}",
        children=[dcc.Graph(id=f"lineChart_{graph_number}", figure=fig)],
    )


def bar_one_timepoint(data: Data, graph_number: int = 1) -> Any:
    data_: Dict[str, Any] = data["data"][0]
    values: List[int] = list(data_.values())
    items: List[Tuple[str, int]] = sorted(
        list(data_.items())[1:], key=lambda item: item[1], reverse=True
    )
    thresh: float = max(values[1:]) * 0.2

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])

    for label, value in items:
        sec_y: bool = False if value > thresh else True
        fig.add_trace(go.Bar(name=label, x=[label], y=[value]), secondary_y=sec_y)

    return html.Div(
        id=f"graphWrapper_{graph_number}",
        children=[dcc.Graph(id=f"barChart_{graph_number}", figure=fig)],
    )
