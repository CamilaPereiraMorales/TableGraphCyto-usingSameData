import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(__name__)

app.config['suppress_callback_exceptions']=True
 
usStates = df.State
for States in usStates:
 #   print(States)

    nodes = [
     
        {
            'data': {'id': short, 'label': States},
            'position': {'x': Capacity, 'y': Generation}
        }
        for short, Generation, Capacity in (
            ('ca',  10826, 4395),
            ('az',  2550, 1078),
            ('nv',  557, -238),
            ('nm', 590, 261),
            ('col',  235, 118),
            ('tex',  354, 187),
            ('nc',  1162, 669),
            ('nyc',  84, 53)
        )
    ]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('ca', 'col'),
        ('col', 'nv'),
        ('tex', 'nm'),
        ('tex', 'nm'),
        ('nc', 'nyc'),
        ('nyc', 'ca'),
        ('nm', 'az'),
        ('ca', 'nyc'),
        ('az', 'nv'),
        ('nyc', 'ca')
    )
]

elements = nodes + edges

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
        row_selectable=True,
        selected_rows=[]
    ),
    html.Div(id='exampleGraph'),
    html.Div(id='update_layout')
  

])

@app.callback(Output('update_layout', 'children'),
             [Input('table',"derived_virtual_data"),
             Input('table',"derived_virtual_selected_rows")])

def update_layout(rows,derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    if rows is None:
        dff = df
    else:
        dff = pd.DataFrame(rows)

    colors = []
    for i in range(len(dff)):
        if i in derived_virtual_selected_rows:
            colors.append("#7FDBFF")
        else:
            colors.append("#0074D9")

    return html.Div(
        [
         cyto.Cytoscape(
                id="cyto",
                layout={'name':'breadthfirst'},
                zoomingEnabled=False,
                elements=elements,
            )

        
        ])


    
@app.callback(
     Output('exampleGraph',"children"),
     [Input('table',"derived_virtual_data"),
      Input('table',"derived_virtual_selected_rows")])

def update_graph(rows,derived_virtual_selected_rows):
     
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    if rows is None:
        dff = df
    else:
        dff = pd.DataFrame(rows)

    colors = []
    for i in range(len(dff)):
        if i in derived_virtual_selected_rows:
            colors.append("#7FDBFF")
        else:
            colors.append("#0074D9")

    return html.Div(
        [
        dcc.Graph(
                id="graph",
                figure={
                    "data": [
                        {
                            "x": df['State'],
                            "y": df["Number of Solar Plants"],
                            "text": df["Average MW Per Plant"],
                            "type":"bar",
                            "marker":{"color":colors},              
                        }
                    ]
                }
            ),
        #  cyto.Cytoscape(
        #         id="cyto",
        #         layout={'name':'breadthfirst'},
        #         zoomingEnabled=True,
        #         elements=elements
        #     )

        
        ])



if __name__ == '__main__':
    app.run_server(debug=True)