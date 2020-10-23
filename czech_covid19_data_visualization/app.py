from typing import Any, List

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from czech_covid19_data_visualization import data
from czech_covid19_data_visualization import graphs

external_stylesheets: List[str] = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app: dash.Dash = dash.Dash(
    name="Czech COVID19 Data Visualizer", external_stylesheets=external_stylesheets
)

app.layout = html.Div(
    id="mainWrapper",
    children=[
        dcc.Store(id="dataStorage", storage_type="memory"),
        html.Div(
            id="headlineWrapper",
            children=[html.H1(id="headline", children="COVID19 Czech Data Visualizer")],
        ),
        html.Div(
            id="menuWrapper",
            children=[
                html.Div(
                    id="dropdownWrapper",
                    children=[
                        dcc.Dropdown(
                            id="dataSelector",
                            options=[
                                {"label": "Number of infected", "value": "infected"},
                                {"label": "Number of tests done", "value": "tests"},
                                {
                                    "label": "Number of infected, cured, deaths and tests done",
                                    "value": "all_numbers",
                                },
                                {"label": "Basic overview", "value": "basic_overview"},
                                {
                                    "label": "Age distribution of cured patients",
                                    "value": "cured",
                                },
                                {
                                    "label": "Age distribution of dead patients",
                                    "value": "dead",
                                },
                                {
                                    "label": "Age distribution of infected patients",
                                    "value": "infected_individuals",
                                },
                            ],
                            value="infected",
                            multi=False,
                        )
                    ],
                )
            ],
        ),
        html.Div(id="divisionWrapper", children=[html.Hr(id="menuSeparator")]),
        html.Div(id="graphicWrapper", children=[]),
        html.Div(
            id="footerWrapper",
            children=[
                html.Div(
                    id="dataSourceWrapper",
                    children=[
                        html.A(
                            id="linkDataSource",
                            href="https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19",
                            target="_blank",
                            children=["Data source"],
                        )
                    ],
                )
            ],
        ),
    ],
)

# CALLBACKS
@app.callback(
    Output(component_id="dataStorage", component_property="data"),
    [
        Input(component_id="dataSelector", component_property="value"),
    ],
)
def store_data(value) -> Any:
    if value is None:
        PreventUpdate()

    else:
        if value == "infected":
            return data.get(data="infected")

        if value == "tests":
            return data.get(data="tests")

        if value == "all_numbers":
            return data.get(data="all_numbers")

        if value == "basic_overview":
            return data.get(data="basic_overview")

        if value == "cured":
            return data.get(data="cured")

        if value == "dead":
            return data.get(data="dead")

        if value == "infected_individuals":
            return data.get(data="infected_individuals")


@app.callback(
    Output(component_id="graphicWrapper", component_property="children"),
    [
        Input(component_id="dataStorage", component_property="data"),
        Input(component_id="dataSelector", component_property="value"),
    ],
)
def display_data(data, value) -> Any:
    if data is None:
        PreventUpdate()

    else:
        if value == "infected":
            return graphs.vertical_bar_and_line_2inputs(data, graph_number=1)

        if value == "tests":
            return graphs.vertical_bar_and_line_2inputs(data, graph_number=1)

        if value == "all_numbers":
            return graphs.line_3inputs(data, graph_number=1)

        if value == "basic_overview":
            return graphs.bar_one_timepoint(data, graph_number=1)

        if value == "cured":
            return graphs.histogram(data, graph_number=1)

        if value == "dead":
            return graphs.histogram(data, graph_number=1)

        if value == "infected_individuals":
            return graphs.histogram(data, graph_number=1)
