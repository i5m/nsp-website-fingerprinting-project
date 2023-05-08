import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import pandas as pd

# Read the data.
data = pd.read_csv('./fingerprints - data.csv')

data.columns = ["domain", "total_incoming_sizes", "total_number_packets", "no_outgoing_packets", "no_incoming_packets", "ratio_incoming_to_outgoing", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]

d = data['domain']
#x = data['total_number_packets']
#y = data['no_incoming_packets']
#z = data['no_outgoing_packets']
x = data['total_incoming_sizes']
y = data['ratio_incoming_to_outgoing']
z = data['total_number_packets']

xt = []
yt = []
zt = []
data = []

for i in range(0, len(x)):
    if i == len(x) - 1 or d[i] != d[i + 1]:
        data.append(go.Scatter3d(x=xt, y=yt, z=zt, mode='markers', \
            marker=dict(), name=d[i]))

        xt = []
        yt = []
        zt = []
    else:
        xt.append(x[i])
        yt.append(y[i])
        zt.append(z[i])

layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))

fig = go.Figure(data=data, layout=layout)
pio.write_html(fig, file='graph.html', auto_open=True)

