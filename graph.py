# All necessary imports
from scipy.stats import binom
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Generating random data and counting the numbers
n = 1024
size = 1000
prob = 0.1
x = np.arange(70, 135)
yy = []
tt = []

for a in range(1500):
    y = binom.rvs(n, prob, size=size)
    d = pd.DataFrame(y, columns  = ['Data'])
    
    for k in range(len(x)):
        yy.append(d[d['Data'] == x[k]].count()[0])
        
    tt.append(yy)
    yy = []
    y = []

kk = pd.DataFrame(tt).T
y = kk.mean(axis=1)
N = len(y)

data = pd.DataFrame([x,y]).T
data.columns = ['Score', 'Frequency']

# Plotting the graph
fig = go.Figure(
    data=[go.Scatter(x=data['Score'], y=data['Frequency'],
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[data['Score'].min(), data['Score'].max()], autorange=False),
        yaxis=dict(range=[data['Frequency'].min(), data['Frequency'].max()+2], autorange=False),
        title="Binomial Curve",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ))


fig.show()