from dash.dependencies import Input, Output
from components import plot_map
from config import data

 @app.callback(
        Output("france-map", "figure"),
        [
            Input("departments-dropdown", "value"),
        ],
    )                                               
    def department_zoom(value):
        for index,val in enumerate(data["dep_name"]):
            if val==value:
                lat = data["lat"][index]
                long = data["long"][index]
                zoom = data["zoom"][index]
        return plot_map(lat,long,zoom)

