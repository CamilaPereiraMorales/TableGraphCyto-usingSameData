import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df.columns = [c.lower().replace(' ', '_') for c in df.columns]
df.columns = [c.replace('(', '') for c in df.columns]
df.columns = [c.replace(')', '') for c in df.columns]

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions']=True

usStates = df.state
#print(usStates)


nodes=[]
for index, row in df.iterrows():
    nodes.append({'data': {'id': row['state'], 'label': row['state']}, 'position': {'x': row['number_of_solar_plants'], 'y': row['installed_capacity_mw']}})

#print(nodes)

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('California', 'Colorado'),
        ('Colorado', 'Nevada'),
        ('Texas', 'New Mexico'),
        ('Texas', 'New Mexico'),
        ('North Carolina', 'New York'),
        ('New York', 'California'),
        ('New Mexico', 'Arizona'),
        ('California', 'New York'),
        ('Arizona', 'Nevada'),
        ('New York', 'California')
    )
]



elements = nodes + edges
#print(elements)


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

    colors2 = []
    for i in range(len(dff)):
        if i in derived_virtual_selected_rows:
            colors2.append("#7FDBFF")
        else:
            colors2.append("#0074D9")

    return html.Div(
        [
        dcc.Graph(
                id="graph",
                figure={
                    "data": [
                        {
                            "x": df['state'],
                            "y": df["number_of_solar_plants"],
                            "text": df["average_mw_per_plant"],
                            "type":"bar",
                            "marker":{"color":colors2},              
                        }
                    ]
                }
            ),
         cyto.Cytoscape(
                id="cytoscape-stylesheet-callbacks",
                layout={'name':'circle'},
                zoomingEnabled=True,
                elements=elements
            )

        
        ])
        
@app.callback(Output('cytoscape-stylesheet-callbacks', 'stylesheet'),
              [Input('input-line-color', 'value'),
               Input('input-bg-color', 'value')])
def update_stylesheet(line_color, bg_color):
    if line_color is None:
        line_color = ''

    if bg_color is None:
        bg_color = ''

    new_styles = [
        {
            'selector': 'node',
            'style': {
                'background-color': bg_color
            }
        },
        {
            'selector': 'edge',
            'style': {
                'line-color': line_color
            }
        }
    ]

    return default_stylesheet + new_styles


if __name__ == '__main__':
    app.run_server(debug=True)