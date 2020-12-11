from typing import Any, Dict, List, Optional, Tuple, Union

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from pandas import DataFrame, Series
from plotly.subplots import make_subplots

from czech_covid19_data_visualization.data import (
    transform_for_delta,
    transform_for_histogram,
    transform_for_index,
)
from czech_covid19_data_visualization.io import get_screen_res

# pylint: disable=unsubscriptable-object
Data = Dict[str, Union[str, List[Dict[str, Any]]]]

screen_res: Any = get_screen_res()
WIDTH_MOD: float = 0.9
HEIGHT_MOD: float = 0.65


def vertical_bar_and_line_2inputs(data: Data, graph_number: int = 1) -> Any:
    try:
        df: DataFrame = DataFrame.from_records(data["data"])
        labels: List[str] = [item.replace("_", " ").capitalize() for item in df.columns]

        fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Bar(name=labels[1], x=df.iloc[:, 0], y=df.iloc[:, 1]), secondary_y=False
        )
        fig.add_trace(
            go.Scatter(name=labels[2], x=df.iloc[:, 0], y=df.iloc[:, 2]),
            secondary_y=True,
        )
        fig.update_layout(
            autosize=False,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"barLineChart_{graph_number}", figure=fig)],
        )
    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )


def line_3inputs(data: Data, graph_number: int = 1) -> Any:
    try:
        df: DataFrame = DataFrame.from_records(data["data"])
        labels: List[str] = [item.replace("_", " ").capitalize() for item in df.columns]

        fig: Any = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(name=labels[1], x=df.iloc[:, 0], y=df.iloc[:, 1]),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(name=labels[2], x=df.iloc[:, 0], y=df.iloc[:, 2]),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(name=labels[3], x=df.iloc[:, 0], y=df.iloc[:, 3]),
            secondary_y=True,
        )
        fig.update_layout(
            autosize=False,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"lineChart_{graph_number}", figure=fig)],
        )
    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )


def bar_one_timepoint(data: Data, graph_number: int = 1) -> Any:
    try:
        data_: Dict[str, Any] = data["data"][0]
        values: List[int] = list(data_.values())
        items: List[Tuple[str, int]] = sorted(
            list(data_.items())[1:10], key=lambda item: item[1], reverse=True
        )
        thresh: float = max(values[1:10]) * 0.2

        fig: Any = make_subplots(specs=[[{"secondary_y": True}]])

        for label, value in items:
            label = label.replace("_", " ").capitalize()
            sec_y: bool = False if value > thresh else True
            fig.add_trace(
                go.Bar(
                    name=label, x=[label], y=[value], text=value, textposition="auto"
                ),
                secondary_y=sec_y,
            )
        fig.update_layout(
            autosize=False,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"barChart_{graph_number}", figure=fig)],
        )
    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )


def histogram(data: Any, graph_number: int = 1) -> Any:
    try:
        data_: Dict[str, Any] = data["data"]
        transformed_data: Dict[str, Any] = transform_for_histogram(data_)

        fig: Any = make_subplots(rows=1, cols=len(list(transformed_data.keys())))
        for i, key in enumerate(list(transformed_data.keys())):
            fig.append_trace(
                go.Histogram(
                    name=key.capitalize(),
                    x=transformed_data[key],
                    xbins=dict(start=0.0, end=110.0, size=10.0),
                ),
                1,
                i + 1,
            )
        fig.update_layout(
            autosize=False,
            bargap=0.05,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )
        fig.update_yaxes(automargin=True)

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"histogram_{graph_number}", figure=fig)],
        )
    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )


def index_line(label: str, data_one: Any, data_two: Any, graph_number: int = 1) -> Any:
    try:
        (data, trend) = transform_for_index(data_one, data_two)

        fig: Any = make_subplots()
        fig.add_trace(
            go.Scatter(x=data.index, y=data, mode="lines", name=label, text=data)
        )
        fig.add_trace(
            go.Scatter(x=data.index, y=trend, mode="lines", name="trend (7D MA)")
        )
        fig.update_layout(
            showlegend=True,
            autosize=False,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"indexLineGraph_{graph_number}", figure=fig)],
        )
    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )


def delta_bar_and_line(label: str, data: Any, graph_number: int = 1) -> Any:
    try:
        (original, delta) = transform_for_delta(data)

        fig: Any = make_subplots(rows=2, cols=1)
        fig.append_trace(go.Bar(x=delta.index, y=delta, name="7-day delta"), 1, 1)
        fig.append_trace(go.Bar(x=original.index, y=original, name=label), 2, 1)
        fig.update_layout(
            showlegend=True,
            autosize=False,
            width=screen_res.width * WIDTH_MOD,
            height=screen_res.height * HEIGHT_MOD,
        )
        fig.update_yaxes(automargin=True)

        return html.Div(
            id=f"graphWrapper_{graph_number}",
            children=[dcc.Graph(id=f"deltaBarLineGraph_{graph_number}", figure=fig)],
        )

    except Exception as e:
        return html.Div(
            id=f"exceptionInfoWrapper_{graph_number}",
            children=[f"Graph could not be rendered. Exception: {str(e)}"],
        )
