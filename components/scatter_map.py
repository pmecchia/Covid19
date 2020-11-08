import pandas as pd
import plotly.express as px
from config import *



px.set_mapbox_access_token(MAPBOX_ACCESS_TOKEN)

def plot_map(lat=46.4,lon=0.5,zoom=3.5):    
    
    color_scale = ["#fadc8f",
        "#f9d67a",
        "#f8d066",
        "#f8c952",
        "#f7c33d",
        "#f6bd29",
        "#f5b614",
        "#F4B000",
        "#eaa900",
        "#e0a200",
        "#dc9e00",]
    
    fig = px.scatter_mapbox(
        df_last_update,
        lat = "lat",
        lon = "long",
        color = "nb_pos_cum",
        size="scaled",
        size_max = 35,
        hover_name = "dep_name",
        hover_data = ["nb_pos_cum","dc","death_rate","dep_name"],
        color_continuous_scale = color_scale,
    )

    fig.layout.update(
            mapbox_style="dark",
            mapbox=dict(center=dict(lat=lat, lon=lon), zoom=zoom),
        )
    fig.data[0].update(
            hovertemplate=("%{customdata[3]}<br>Confirmed:"
                          " %{customdata[0]}<br>Deaths: %{customdata[1]}@<br>Death Rate: %{customdata[2]}")
        )

    return fig