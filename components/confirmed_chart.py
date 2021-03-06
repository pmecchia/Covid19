import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils.data import DF_FRANCE,DF_DEPARTMENTS


def confirmed_cases(department,last_days_nb): 
    
    #select dataframe 
    if department == "France":
        selected_df=DF_FRANCE
    else:
        selected_df=DF_DEPARTMENTS[DF_DEPARTMENTS["dep_name"]==department]
        
    yaxis_max=np.log10(selected_df['Confirmed'].tail(1).tolist()[0])+0.5    
    fig_confirmed = go.Figure()
    fig_confirmed.add_trace(
        go.Scatter(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['Confirmed'].tail(last_days_nb),
            mode="lines",
            line={"color":"#dc9e00"},
            showlegend=False,
        )
    )
    fig_confirmed.add_trace(
        go.Bar(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['nb_pos'].tail(last_days_nb),
            marker={"color":"#f9d67a"},
            showlegend=False,

        )
    )


    # LINE CHART ANNOTATION
    fig_confirmed.add_annotation(
         x=selected_df['jour'].tail(last_days_nb).tolist()[0],
         y=yaxis_max,
         text="Total Confirmed Cases",
         font={"size": 14,"color":"#dc9e00"},
         xshift=100,  # Annotation x displacement!
         showarrow=False,
    )

    # BAR CHART ANNOTATION
    fig_confirmed.add_annotation(
        x=selected_df['jour'].tail(last_days_nb).tolist()[0],
        y=np.log10(selected_df['nb_pos'].tail(last_days_nb).max()),
        text="New Confirmed Cases",
        font={"size": 14, "color":"#f9d67a"},
        xshift=350,  # Annotation x displacement!
        yshift=10,  # Annotation y displacement!
        showarrow=False,
        )
    fig_confirmed.update_layout(
        template="plotly_dark",
        xaxis={"title":"Dates"},
        yaxis=dict(range=[0,yaxis_max],title="Number of cases"),
        yaxis_type="log",
        autosize=True,
        margin={"r":0,"t":23,"l":0,"b":0},
        
    )
    
    return fig_confirmed