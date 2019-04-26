# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#99FFCC',
    'text': '#6666FF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    ''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [4, 1, 2, 3, 5], 'type': 'cake', 'name': 'SF'},
                {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 1, 7], 'type': 'cake', 'name': u'Montréal'},
                {'x': [1, 2, 2.5, 3, 4, 5], 'y': [1, 2, 7, 4, 5, 2], 'type': 'cake', 'name': 'La Habana'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)