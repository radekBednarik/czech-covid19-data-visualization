from typing import Any, List

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from czech_covid19_data_visualization import data, graphs, io

external_stylesheets: List[str] = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
api_data: Any = data.get_all_data()

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
                            options=[
                                {"label": "Number of infected", "value": "infected"},
                                {
                                    "label": "7D Delta: Number of infected",
                                    "value": "infected_delta",
                                },
                                {"label": "Number of tests done", "value": "tests"},
                                {
                                    "label": "Infected to tests done ratio",
                                    "value": "infected_to_tests",
                                },
                                {
                                    "label": "Number of infected, cured and deaths",
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
                            value="basic_overview",
                            multi=False,
                        )
                    ],
                )
            ],
        ),
        html.Div(id="divisionWrapper", children=[html.Hr(id="menuSeparator")]),
        dcc.Loading(
            id="loadingGraphicOverlay",
            children=[
                html.Div(id="graphicWrapper", children=[]),
            ],
            type="cube",
        ),
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


@app.callback(
    Output(component_id="graphicWrapper", component_property="children"),
    [Input(component_id="dataSelector", component_property="value")],
)
def display_data(value) -> Any:
    if value is None:
        PreventUpdate()

    else:
        if value == "infected":
            return graphs.vertical_bar_and_line_2inputs(
                api_data["infected"], graph_number=1
            )

        if value == "infected_delta":
            data_infected: Any = api_data["infected"]
            return graphs.delta_bar_and_line(
                "Daily number of infected",
                {"prirustkovy_pocet_nakazenych": data_infected},
                graph_number=1,
            )

        if value == "tests":
            return graphs.vertical_bar_and_line_2inputs(
                api_data["tests"], graph_number=1
            )

        if value == "all_numbers":
            return graphs.line_3inputs(api_data["all_numbers"], graph_number=1)

        if value == "basic_overview":
            return graphs.bar_one_timepoint(api_data["basic_overview"], graph_number=1)

        if value == "cured":
            return graphs.histogram(api_data["cured"], graph_number=1)

        if value == "dead":
            return graphs.histogram(api_data["dead"], graph_number=1)

        if value == "infected_individuals":
            return graphs.histogram(api_data["infected_individuals"], graph_number=1)

        if value == "infected_to_tests":
            data_one: Any = api_data["infected"]
            data_two: Any = api_data["tests"]
            return graphs.index_line(
                "Infected to tests done ratio",
                {"prirustkovy_pocet_nakazenych": data_one},
                {"prirustkovy_pocet_testu": data_two},
                graph_number=1,
            )


def main() -> None:
    app.run_server(debug=False, dev_tools_hot_reload=False)


if __name__ == "__main__":
    main()
