from typing import List
from utils.data import DF_FRANCE,DF_LAST_UPDATE
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np


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
        
    number_new_test=df_selected.iloc[0]["nb_test"]
    number_test = df_selected.iloc[0]["nb_test_cum"]
    number_new_pos=df_selected.iloc[0]["nb_pos"]
    number_pos=df_selected.iloc[0]["Confirmed"]
    number_new_dc=df_selected.iloc[0]["new_dc"]
    number_dc=df_selected.iloc[0]["dc"]
    new_death_rate=df_selected.iloc[0]["new_death_rate"]
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
                                f"+{number_new_test:,} new",
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                f"{number_test:,}",
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
        elif columns == "Confirmed":
            card = dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.P(
                                f"+{number_new_pos:,} new",
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                f"{number_pos:,}",
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
                                f"+{number_new_dc:,} new",
                                className=f"top-bar-change-{columns.lower()}",
                            ),
                            html.H1(
                                f"{number_dc:,}",
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
                                f"{new_death_rate:+.2f}% change",
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
            
    #change card positions
    cards[0], cards[1] = cards[1], cards[0]
    cards[1], cards[2] = cards[2], cards[1]
    
        
    return cards