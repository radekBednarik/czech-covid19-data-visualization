from typing import Any, Dict, List

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots


def vertical_bar_and_line_2inputs(
    data: List[Dict[str, Any]], graph_number: int = 1
) -> Any:
    df: DataFrame = DataFrame.from_records(data)
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


def line_3inputs(data: List[Dict[str, Any]], graph_number: int = 1) -> Any:
    df: DataFrame = DataFrame.from_records(data)
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


def bar_one_timepoint_overview(
    data: List[Dict[str, Any]], graph_number: int = 1
) -> Any:
    x: List[str] = list(data[0].keys())
    data_: Dict[str, int] = data[0]

    fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=[x[1]], y=[data_["provedene_testy_celkem"]]), secondary_y=False
    )
    fig.add_trace(
        go.Bar(x=[x[2]], y=[data_["potvrzene_pripady_celkem"]]), secondary_y=False
    )
    fig.add_trace(go.Bar(x=[x[3]], y=[data_["aktivni_pripady"]]), secondary_y=False)
    fig.add_trace(go.Bar(x=[x[4]], y=[data_["vyleceni"]]), secondary_y=False)
    fig.add_trace(go.Bar(x=[x[5]], y=[data_["umrti"]]), secondary_y=True)
    fig.add_trace(
        go.Bar(x=[x[6]], y=[data_["aktualne_hospitalizovani"]]), secondary_y=True
    )
    fig.add_trace(
        go.Bar(x=[x[7]], y=[data_["provedene_testy_vcerejsi_den"]]), secondary_y=True
    )
    fig.add_trace(
        go.Bar(x=[x[8]], y=[data_["potvrzene_pripady_vcerejsi_den"]]), secondary_y=True
    )
    fig.add_trace(
        go.Bar(x=[x[9]], y=[data_["potvrzene_pripady_dnesni_den"]]), secondary_y=True
    )

    return html.Div(
        id=f"graphWrapper_{graph_number}",
        children=[dcc.Graph(id=f"barChart_{graph_number}", figure=fig)],
    )
