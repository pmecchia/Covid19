from typing import List
from utils.data import DF_FRANCE,DF_LAST_UPDATE
import dash_bootstrap_components as dbc
import dash_html_components as html


def daily_results(department="France") -> List[dbc.Col]:
    """Returns a top bar as a list of Plotly dash components displaying
    tested, confirmed, and death cases for the top row.
    :param none: none
    :return cols: A list of plotly dash boostrap components Card objects
    displaying tested, confirmed, deaths.
    """
    if department=="France":
        df_selected=DF_FRANCE.tail(1)
    else:
        df_selected=DF_LAST_UPDATE.loc[DF_LAST_UPDATE["dep_name"]==department]
        

    # 2. Dynamically generate list of dbc Cols. Each Col contains a single
    #    Card. Each card displays items and values 
    cards = []
    card=0
    for columns in df_selected:
        if columns == "nb_test_cum":
            card = dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                df_selected["nb_test"],
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                df_selected[columns],
                                className=f"top-bar-value-{columns.lower()}",
                            ),
                            html.P(
                                "Tested",
                                className="card-text",
                            ),
                        ],
                    ),
                    className=f"top-bar-card-{columns.lower()}",
                ),
                className="top-bar-card-body",
                width=2.5,
            )
        elif columns == "nb_pos_cum":
            card = dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                df_selected["nb_pos"],
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                df_selected[columns],
                                className=f"top-bar-value-{columns.lower()}",
                            ),
                            html.P(
                                "Confirmed",
                                className="card-text",
                            ),
                        ]
                    ),
                    className=f"top-bar-card-{columns.lower()}",
                ),
                width=2.5,
                className="top-bar-card-body",
            )
        elif columns == "dc":
            card = dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                df_selected["new_dc"],
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                df_selected[columns],
                                className=f"top-bar-value-{columns.lower()}",
                            ),
                            html.P("Deaths", className="card-text"),
                        ]
                    ),
                    className=f"top-bar-card-{columns.lower()}",
                ),
                width=2.5,
                className="top-bar-card-body",
            )
        elif columns == "death_rate":
            card = dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                round(df_selected["new_death_rate"],2),
                                className=f"top-bar-perc-change-{columns.lower()}",
                            ),
                            html.H1(
                                df_selected[columns],
                                className=f"top-bar-value-{columns.lower()}",
                            ),
                            html.P("Death Rate", className="card-text"),
                        ]
                    ),
                    className=f"top-bar-card-{columns.lower()}",
                ),
                width=2.5,
                className="top-bar-card-body",
            )
        if card != 0:
            cards.append(card)
            card=0
        
    return cards