import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils.data import DF_FRANCE,DF_DEPARTMENTS


def covid_deaths(department,last_days_nb):  
    
    #select dataframe according to department value
    if department == "France":
        selected_df=DF_FRANCE
    else:
        selected_df=DF_DEPARTMENTS[DF_DEPARTMENTS["dep_name"]==department]
    
    yaxis_max=np.log10(selected_df['dc'].tail(1).tolist()[0])+0.5
    fig_deaths = go.Figure()
    fig_deaths.add_trace(
        go.Scatter(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['dc'].tail(last_days_nb),
            mode="lines",
            line={"color":"#c94904"},
            showlegend=False,
            #name="Total Confirmed Cases"
        )
    )
    fig_deaths.add_trace(
        go.Bar(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['new_dc'].tail(last_days_nb),
            marker={"color":"#d6885e"},
            showlegend=False,
            #name="New Confirmed Cases",

        )
    )


    # LINE CHART ANNOTATION
    fig_deaths.add_annotation(
         x=selected_df['jour'].tail(last_days_nb).tolist()[0],
         y=yaxis_max,
         text="Total Deaths",
         font={"size": 14,"color":"#c94904"},
         xshift=100,  # Annotation x displacement!
         showarrow=False,
    )

    # BAR CHART ANNOTATION
    fig_deaths.add_annotation(
        x=selected_df['jour'].tail(last_days_nb).tolist()[0],
        y=np.log10(selected_df['new_dc'].tail(last_days_nb).max()),
        text="New Deaths",
        font={"size": 14, "color":"#d6885e"},
        xshift=350,  # Annotation x displacement!
        yshift=10,  # Annotation y displacement!
        showarrow=False,
        )
    fig_deaths.update_layout(
        template="plotly_dark",
        xaxis={"title":"Dates"},
        yaxis=dict(range=[0,yaxis_max],title="Number of deaths"),
        yaxis_type="log",
        autosize=True,
        margin={"r":0,"t":23,"l":0,"b":0},
    )
    return fig_deaths