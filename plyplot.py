import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np


df = pd.read_csv('truecollector.csv')

print(df['red_h'])

expansion_list = list(set(df['expansion']))
hexval_list = list(df['hexval'])
# name_list = list(df['name'])
madlist = list(df['codename'])
colormap = dict(zip(madlist, hexval_list))

fig = go.Figure(data=[go.Scatter3d(
    x=df['red_h'],
    y=df['green_h'],
    z=df['blue_h'],
    mode='markers',
    marker=dict(
        size=8,
        color=hexval_list,                # set color to an array/list of desired values
        #colorscale='Viridis',   # choose a colorscale
        opacity=0.15
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()