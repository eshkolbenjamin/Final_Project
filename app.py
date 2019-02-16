import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd


import plotly.plotly as py
import plotly.graph_objs as go

########### Set up the chart

df = pd.read_csv('/Users/eshkol/Desktop/Python/EB/Dataset/titanic.csv')

results = df.groupby(['Sex','Pclass']).Age.mean()

trace1 = go.Bar(
    x=['Class 1', 'Class 2', 'Class 3'],
    y=[results[3],results[4],results[5]],
    name='Male'
)
trace2 = go.Bar(
    x=['Class 1', 'Class 2', 'Class 3'],
    y=[results[0],results[1],results[2]],
    name='Female'
)

data = [trace1, trace2]
layout = go.Layout(
    title='Average age of passengers by class',
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Titanic'),
    dcc.Graph(
        id='flyingdog',
        figure=fig
    )]
)

if __name__ == '__main__':
    app.run_server()
