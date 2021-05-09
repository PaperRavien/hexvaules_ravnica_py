import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np


df = pd.read_csv('truecollector.csv')

#print(df['red_h'])
RAVdata = df.loc[df['expansion'].isin(['RAV'])]
GPTdata = df.loc[df['expansion'].isin(['GPT'])]
DISdata = df.loc[df['expansion'].isin(['DIS'])]
RTRdata = df.loc[df['expansion'].isin(['RTR'])]
GTCdata = df.loc[df['expansion'].isin(['GTC'])]
DGMdata = df.loc[df['expansion'].isin(['DGM'])]
GRNdata = df.loc[df['expansion'].isin(['GRN'])]
RNAdata = df.loc[df['expansion'].isin(['RNA'])]
WARdata = df.loc[df['expansion'].isin(['WAR'])]


expansion_list = list(set(df['expansion']))
hexval_list = list(df['hexval'])
# name_list = list(df['name'])
madlist = list(df['codename'])
colormap = dict(zip(madlist, hexval_list))
#print(colormap)

fig = go.Figure(data=[go.Scatter3d(
    # x=df['red_h'],
    # y=df['green_h'],
    # z=df['blue_h'],
    mode='markers',
    hover_name = RAVdata['name'],
    marker=dict(
        size=8,
        color=hexval_list, # set color to an array/list of desired values
        #colorscale='Viridis',   # choose a colorscale
        opacity=0.2
    )
)])

#just the logo is blocking it so removing some space
fig.add_trace(go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    name="skipdata",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color='white',
        opacity=0.05)
    )
)
fig.add_trace(go.Scatter3d(
    x=[255],
    y=[255],
    z=[255],
    name="|||||||||||||",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color='white',
        opacity=0.05)
    )
)
#ALL THE SECTIONS HERE

fig.add_trace(go.Scatter3d(
    x=RAVdata['red_h'],
    y=RAVdata['green_h'],
    z=RAVdata['blue_h'],
    name="RAV",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=RAVdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=GPTdata['red_h'],
    y=GPTdata['green_h'],
    z=GPTdata['blue_h'],
    name="GPT",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=GPTdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=DISdata['red_h'],
    y=DISdata['green_h'],
    z=DISdata['blue_h'],
    name="DIS",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=DISdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=RTRdata['red_h'],
    y=RTRdata['green_h'],
    z=RTRdata['blue_h'],
    name="RTR",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=RTRdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=GTCdata['red_h'],
    y=GTCdata['green_h'],
    z=GTCdata['blue_h'],
    name="GTC",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=GTCdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=DGMdata['red_h'],
    y=DGMdata['green_h'],
    z=DGMdata['blue_h'],
    name="DGM",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=DGMdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=GRNdata['red_h'],
    y=GRNdata['green_h'],
    z=GRNdata['blue_h'],
    name="GRN",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=GRNdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=RNAdata['red_h'],
    y=RNAdata['green_h'],
    z=RNAdata['blue_h'],
    name="RNA",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=RNAdata['hexval'],
        opacity=0.5)
    )
)

fig.add_trace(go.Scatter3d(
    x=WARdata['red_h'],
    y=WARdata['green_h'],
    z=WARdata['blue_h'],
    name="WAR",
    #visible='legendonly',
    mode='markers',
    marker=dict(
        size=8,
        color=WARdata['hexval'],
        opacity=0.5)
    )
)
# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()