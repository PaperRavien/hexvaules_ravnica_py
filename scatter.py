import pandas as pd
import plotly.express as px
import plotly.io as pio
#import random as rng

#from tqdm import tqdm


# import numpy as np
# import plotly.graph_objects as go

#Use for animiation rotation at the end
x_eye = -1.25
y_eye = 2
z_eye = 0.5

df = pd.read_csv('truecollector.csv')
# print(df)
expansion_list = list(set(df['expansion']))
hexval_list = list(df['hexval'])
# name_list = list(df['name'])
madlist = list(df['codename'])
colid = list(set(df['colourid']))
print(colid)
colormap = dict(zip(madlist, hexval_list))
#df = df[df['expansion'].isin(expansion_list)]
#print(df['expansion'])
#expansions = set(df['expansion'])
#df = df[df['expansion'].isin(expansions)]
# df = df[df['expansion'].isin(['RAV','GPT'])]
#df = df[df['hexval'].isin(hexval_list)]
# df = df[df['name'].isin(name_list)]
#df = df[df['codename'].isin(madlist)]
# df = df[df['colourid'].isin(colid)]
#df = df[df['']]
#df = df[df['name'].isin([])]
#df = df[df['']]

# print("finished setting up data...")
# print("loading")
# print(df['codename'])
# fig = px.scatter_3d(
# 	data_frame = df,
# 	x = 'red_h',
# 	y = 'green_h',
# 	z = 'blue_h',
# 	color="name",
# 	#color="hexval",
# 	#color="codename",
# 	#color="colourid",
# 	# color = "expansion",
# 	#If hexval color, map needs to be a dict with either identity or name map. The only problem is that there are same names throughout time.
# 	color_discrete_sequence = hexval_list,
# 	#color_discrete_map = colormap,
# 	#color_discrete_sequence=[f'rgb({rng.randint(0,255)},{rng.randint(0,255)},{rng.randint(0,255)})'],
# 	#color_continuous_scale
# 	# color_discrete_sequence=[],
# 	opacity=0.3,
	
# 	# log_x = True,
# 	# log_y = True,
# 	# log_z = True,
# 	#template ='ggplot2',
# 	#template = 'simple_white',
# 	# seaborn, simple_white, plotly, plotly_white, plotly_dark, presentation, xgridoff, ygridoff, gridon, none
# 	title = 'Colour Palettes Database',
# 	labels = {'red_h':'red','green_h':'green','blue_h':'blue'},
# 	hover_name = 'name',
# 	height = 1200,
# 	)

# #fig.write_html("namehex.html")
# pio.show(fig)
# fig.show()
#pio.show(fig, renderer='colab')
