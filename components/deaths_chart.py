import plotly.express as px
import plotly.graph_objects as go
from utils.data import DF_FRANCE,DF_DEPARTMENTS


def covid_deaths(department,last_days_nb):  
    
    #select dataframe according to department value
    if department == "France":
        selected_df=DF_FRANCE
    else:
        selected_df=DF_DEPARTMENTS[DF_DEPARTMENTS["dep_name"]==department]
    
    fig_deaths = go.Figure()
    fig_deaths.add_trace(
        go.Scatter(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['dc'].tail(last_days_nb),
            mode="lines",
            line={"color":"#C616C4"},
            showlegend=False,
            #name="Total Confirmed Cases"
        )
    )
    fig_deaths.add_trace(
        go.Bar(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['new_dc'].tail(last_days_nb),
            marker={"color":"#C616C4"},
            showlegend=False,
            #name="New Confirmed Cases",

        )
    )


    # LINE CHART ANNOTATION
    fig_deaths.add_annotation(
         x=selected_df['jour'].tail(1).tolist()[0],
         y=selected_df['dc'].tail(1).tolist()[0],
         text="Total Deaths",
         font={"size": 14,"color":"#ffffff"},
         xshift=-220,  # Annotation x displacement!
         showarrow=False,
    )

    # BAR CHART ANNOTATION
    fig_deaths.add_annotation(
        x=selected_df['jour'].tail(1).tolist()[0],
        y=selected_df['new_dc'].tail(1).max(),
        text="New Deaths",
        font={"size": 14, "color":"#ffffff"},
        xshift=-60,  # Annotation x displacement!
        yshift=20,  # Annotation y displacement!
        showarrow=False,
        )
    fig_deaths.update_layout(
        template="plotly_dark",
        xaxis={"title":"Dates"},
        yaxis={"title":"Number of deaths"},
        autosize=True,
    )
    return fig_deaths