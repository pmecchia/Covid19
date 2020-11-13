import plotly.express as px
from token_config import MAPBOX_ACCESS_TOKEN
from utils.data import DF_LAST_UPDATE




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
        DF_LAST_UPDATE,
        lat = "lat",
        lon = "long",
        color = "Confirmed",
        size="scaled",
        size_max = 35,
        hover_name = "dep_name",
        hover_data = ["Confirmed","dc","death_rate","dep_name"],
        color_continuous_scale = color_scale,
        
    )

    fig.layout.update(
            margin={"r":0,"t":15,"l":0,"b":15},
            mapbox_style="dark",
            mapbox=dict(center=dict(lat=lat, lon=lon), zoom=zoom),
            font = dict(color = 'white'),
        )
    fig.data[0].update(
            hovertemplate=("%{customdata[3]}<br>Confirmed:"
                          " %{customdata[0]}<br>Deaths: %{customdata[1]}<br>Death Rate: %{customdata[2]}")
        )
    return fig