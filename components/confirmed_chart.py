import plotly.express as px
import plotly.graph_objects as go
from utils.data import DF_FRANCE,DF_DEPARTMENTS


def confirmed_cases(department,last_days_nb): 
    if department == "France":
        selected_df=DF_FRANCE
    else:
        selected_df=DF_DEPARTMENTS[DF_DEPARTMENTS["dep_name"]==department]
        
    fig_confirmed = go.Figure()
    fig_confirmed.add_trace(
        go.Scatter(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['Confirmed'].tail(last_days_nb),
            mode="lines",
            line={"color":"#dc9e00"},
            showlegend=False,
            #name="Total Confirmed Cases"
        )
    )
    fig_confirmed.add_trace(
        go.Bar(
            x=selected_df['jour'].tail(last_days_nb),
            y=selected_df['nb_pos'].tail(last_days_nb),
            marker={"color":"#dc9e00"},
            showlegend=False,
            #name="New Confirmed Cases",

        )
    )


    # LINE CHART ANNOTATION
    fig_confirmed.add_annotation(
         x=selected_df['jour'].tail(1).tolist()[0],
         y=selected_df['Confirmed'].tail(1).tolist()[0],
         text="Total Confirmed Cases",
         font={"size": 14,"color":"#ffffff"},
         xshift=-220,  # Annotation x displacement!
         showarrow=False,
    )

    # BAR CHART ANNOTATION
    fig_confirmed.add_annotation(
        x=selected_df['jour'].tail(1).tolist()[0],
        y=selected_df['nb_pos'].tail(1).max(),
        text="New Confirmed Cases",
        font={"size": 14, "color":"#ffffff"},
        xshift=-60,  # Annotation x displacement!
        yshift=20,  # Annotation y displacement!
        showarrow=False,
        )
    fig_confirmed.update_layout(
        template="plotly_dark",
        xaxis={"title":"Dates"},
        yaxis={"title":"Number of cases"},
        autosize=True,
        margin={"r":0,"t":23,"l":0,"b":0},
    )
    
    return fig_confirmed