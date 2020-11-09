import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from config import DEP_LABELS,TIMESTAMP_LABELS

#Confirm/Death Table

departments_tabs = dbc.Card(
    [
        dbc.CardBody(id="departments-table",className="results-table",),
    ],
    className="results-table-div",
)

#Map

france_map=dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.Div(
                        
                        dcc.Tabs(
                            id="middle-map-tab",
                            value="departments-france-map-tab",
                            colors={
                                "border": None,
                                "primary": None,
                                "background": None,
                            },
                        )
                    ),
                ],
                className="top-bar-france-map",
            ),
            html.Div(
                dcc.Graph(
                    id="france-map",
                    style={"height": "60vh"},
                ),
                id="map-container",
            ),
        ]
    ),
)

#Chart Confirmed Cases

confirmed_chart=dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                id="confirmed-chart-title",
                className="chart-h1-title",
            ),
            html.Div(
                dcc.Dropdown(
                    id="confirmed-lastdays-dropdown",
                    options=TIMESTAMP_LABELS,
                    value="30",
                    clearable=False,
                    searchable=False,
                    className="lastdays-dropdown",
                ),
            ),
            html.Div(
                dcc.Loading(
                    dcc.Graph(
                        id="confirmed-timeline",
                        # figure=cases_chart(),
                        config={"responsive": False},
                        style={"height": "20vh"},
                        className='left-chart-figure"',
                    ),
                ),
                id="confirmed-chart-container",
            ),
        ]
    )
)

#Deaths

deaths_chart=dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                id="deaths-chart-title",
                className="chart-h1-title",
            ),
            html.Div(
                dcc.Dropdown(
                    id="deaths-lastdays-dropdown",
                    options=TIMESTAMP_LABELS,
                    value="30",
                    clearable=False,
                    searchable=False,
                    className="lastdays-dropdown",
                ),
            ),
            html.Div(
                dcc.Loading(
                    dcc.Graph(
                        id="deaths-timeline",
                        # figure=cases_chart(),
                        config={"responsive": False},
                        style={"height": "20vh"},
                        className='right-chart-figure"',
                    ),
                ),
                id="deaths-chart-container",
            ),
        ]
    )
)



build_layout = dbc.Container(fluid=True, children=[
    dbc.Row( #TOP BAR Dayly results
        [
            dbc.Col(
                dcc.Dropdown(
                    id="departments-dropdown",
                    options=DEP_LABELS,
                    value="France",
                    clearable=False,
                    searchable=False,
                    className="departments-dropdown",
                ),
                className="departments-dropdown-container",
                width=2,
            ),
            dbc.Col(
                dbc.Row(id="daily-results", className="top-bar-content"),
                width=10,
                className="top-bar-content-col",
            ),
        ]
    ),
    dbc.Row(#TABLE AND MAP
        [   
            #TABLE
            dbc.Col(
                departments_tabs,
                className="left-column-table-content",
                width=2,
            ),
            #MAP
            dbc.Col(
                html.Div(france_map),
                className="middle-column-map-content",
                width=10,
            )
        ],
        className="middle-content",
    ),
    dbc.Row(#CHARTS
        [
            dbc.Col(
                html.Div(
                    dbc.Row(
                        [   
                            #Confirmed Chart
                            dbc.Col(
                                confirmed_chart,
                                className="top-bottom-left-chart",
                                width=6,
                            ),
                            #Deaths Chart
                            dbc.Col(
                                deaths_chart,
                                className="top-bottom-right-chart",
                                width=6,
                            )
                        ]
                    )
                )
            )
        ]
    )
])