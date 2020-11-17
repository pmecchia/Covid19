from utils.data import DF_DEP_TABLE
import dash_table
from dash_table.Format import Format
import pandas as pd




def departments_results(department):
    
    color_bg = "#000000"
    font_size_body = ".9vw"
    
    table = dash_table.DataTable(
        data=DF_DEP_TABLE.to_dict("records"),
        columns=[
            {"name": "Departments", "id": "Departments",},
            {
                "name": "Confirmed",
                "id": "Confirmed",
                "format": Format(group=","),
            },
            {
                "name": "Deaths",
                "id": "Deaths",
            },
        ],
        editable=False,
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        style_as_list_view=True,
        fixed_rows={"headers": True},
        fill_width=False,
        style_table={
            "width": "100%",
            "height": "50%",
        },
        style_header={
            "backgroundColor": color_bg,
            "border-left": color_bg,
            "border-top": color_bg,
            "border-right": color_bg,
            "border-bottom": "0.01rem solid #313841",
            "fontWeight": "bold",
            "font": "Lato, sans-serif",
            "height": "2vw",
            "textAlign":'left',
            "padding": "1vw",
        },
        style_cell={
            "font-size": font_size_body,
            "font-family": "Lato, sans-serif",
            "border-left": "0",
            "border-right": "0",
            "border-bottom": "0.01rem solid #313841",
            "backgroundColor": "#000000",
            "border": "#000000",
            "color": "#FEFEFE",
            "height": "2.75vw",
            "width":"7vw",
            "textAlign":'center',
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "Departments",},
            },
            {
                "if": {"column_id": "Confirmed",},
                "color": "#dc9e00",
            },
            {
                "if": {"column_id": "Deaths",},
                "color": "#c94904",
            },
        ],
       
    )

    return table