import os
import dash
import dash_bootstrap_components as dbc
from layout.layout_body import build_layout
from callbacks.callbacks import register_callbacks
from utils.data import *


### Initialize Dash app

#dataframes=load_datasets()

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    meta_tags = [{
        "name": "description",
        "content": "Coronavirus statistics and visualizations of number of cases and deaths reported due to the virus."
    }],
)

app.title=("France Coronavirus Tracker")
app.layout = build_layout
server=app.server



#    Register callbacks

register_callbacks(app)
