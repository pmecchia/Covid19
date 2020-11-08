import flask
import dash
import dash_bootstrap_components as dbc

server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    meta_tags = [{
        "name": "description",
        "content": "Coronavirus statistics and visualizations of number of cases and deaths reported due to the virus."
    }]
)


if __name__ == "__main__":
    app.run_server()