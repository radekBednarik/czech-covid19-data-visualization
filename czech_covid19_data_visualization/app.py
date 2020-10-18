import dash
import dash_core_components as dcc
import dash_html_components as html

from typing import List

external_stylesheets: List[str] = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app: dash.Dash = dash.Dash(
    name="Czech COVID19 Data Visualizer", external_stylesheets=external_stylesheets
)

app.layout = html.Div(
    id="mainWrapper",
    children=[
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
                            options=[{"label": "some label", "value": "some value"}],
                        )
                    ],
                )
            ],
        ),
        html.Div(id="divisionWrapper", children=[html.Hr(id="menuSeparator")]),
        html.Div(id="graphicWrapper", children=[]),
    ],
)
