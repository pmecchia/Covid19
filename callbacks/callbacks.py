from dash.dependencies import Input, Output
from components.scatter_map import plot_map
from components.confirmed_chart import confirmed_cases
from components.deaths_chart import covid_deaths
from components.daily_results import daily_results
from components.departments_table import departments_results
from static import data


def register_callbacks(app):
    
    
    
    
    
    #MAP CALLBACK
    
    @app.callback(
        Output("france-map", "figure"),
        [
            Input("departments-dropdown", "value"),
        ],
     )
    def department_zoom(value):
        if value == 'France':
            lat=46.4
            long=0.5
            zoom=3.5
        else:
            for index,val in enumerate(data["dep_name"]):
                if val==value:
                    lat = data["lat"][index]
                    long = data["long"][index]
                    zoom = data["zoom"][index]
        return plot_map(lat,long,zoom)
    
     
    #CONFIRMED CASES CALLBACKS
    
    @app.callback(
        Output("confirmed-timeline", "figure"),
        [
            Input("departments-dropdown", "value"),
            Input("confirmed-lastdays-dropdown","value")
        ],
     )
    def last_confirmed_cases_chart(department,lats_x_days):
        lats_x_days = int(lats_x_days)
        return confirmed_cases(department,lats_x_days)
    
    @app.callback(
        [Output("confirmed-chart-title", "children")],
        [Input("departments-dropdown", "value")],
    )                                                   # pylint: disable=W0612
    def confirmed_cases_chart_title_callback(state="France"):
        return [f"{state} Confirmed Cases"]
    
    #DEATHS CALLBACKS
    
    @app.callback(
        Output("deaths-timeline", "figure"),
        [
            Input("departments-dropdown", "value"),
            Input("deaths-lastdays-dropdown","value")
        ],
     )
    def last_deaths_chart(department,lats_x_days):
        lats_x_days = int(lats_x_days)
        return covid_deaths(department,lats_x_days)
    
    @app.callback(
        [Output("deaths-chart-title", "children")],
        [Input("departments-dropdown", "value")],
    )                                                   # pylint: disable=W0612
    def deaths_chart_title_callback(state="France"):
        return [f"{state} Deaths"]

    #TOP BAR CALLBACK
    @app.callback(
        [Output("daily-results", "children")],
        [Input("departments-dropdown", "value")]
    )
    def daily_results_callback(value):
        cards = daily_results(value) 
        
        return [cards]
    
    #TABLE RESULTS CALLBACK
    @app.callback(
        Output("departments-table", "children"),
        [Input("departments-dropdown", "value")]
    )
    def table_results_callback(value):
        
        return departments_results(value)