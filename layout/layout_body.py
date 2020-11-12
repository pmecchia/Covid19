import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from config import DEP_LABELS,TIMESTAMP_LABELS




#Confirm/Death Table

departments_tabs = dbc.Card(
    [
        dbc.CardBody(
            html.Div(
                id="departments-table",className="results-table",
            ),
        ),
    ],
    className="results-table-div",
)

#Map

france_map=dbc.Card(
    dbc.CardBody(
        [
           
            html.Div(
                dcc.Loading(
                    dcc.Graph(
                        id="france-map",
                        style={"height": "50vh",
                              },
                    ),
                    id="map-container",
                ),
            ),
            
        ]
    ),
    className="map-card",
),
className="france-map-container",

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
                        style={"height": "40vh"},
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
                className="lastdays-dropdown-container"
            ),
            html.Div(
                dcc.Loading(
                    dcc.Graph(
                        id="deaths-timeline",
                        # figure=cases_chart(),
                        config={"responsive": False},
                        style={"height": "40vh"},
                        className='right-chart-figure"',
                    ),
                    style={"padding-top": "8px",},
                    color="#32a852",
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
                width=4,
            ),
            dbc.Col(
                dbc.Row(id="daily-results", className="top-bar-content"),
                width=8,
                className="top-bar-content-col",
            ),
        ],
        className="row-1",
    ),
    
    dbc.Row(#TABLE AND MAP
        [   
            #TABLE
            dbc.Col(
                html.Div(departments_tabs),
                className="left-column-table-content",
                width=4,
            ),
            #MAP
            dbc.Col(
                html.Div(france_map),
                className="middle-column-map-content",
                width=8,
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
                                width=5,
                            ),
                            #Deaths Chart
                            dbc.Col(
                                deaths_chart,
                                className="top-bottom-right-chart",
                                width=5,
                            ),
                        ],
                        #no_gutters=True,  
                        className="test"
                    ),
                    className="bottom-charts"
                ),
                className="bottom-row" 
            ),
        ],
    ),
],
)