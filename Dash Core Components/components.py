import dash
import dash_core_components as dcc
import dash_html_components as html

from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id = 'first-dropdown',
        options = [
            {'label' : 'San Francisco', 'value' : 'SF'},
            {'label' : 'New York City', 'value' : 'NYC'},
            {'label' : 'Santiago', 'value' : 'SCL', 'disabled' : True}
        ],
        # value = 'NYC'
        placeholder = 'Select a City'
        #disabled = True
    ),

    html.Br(),
    html.Br(),

    html.Label('This is a Slider'),
    dcc.Slider(
        min = 1,
        max = 10,
        value = 5,
        marks = {i:i for i in range(10)}
    ),

    html.Br(),
    html.Br(),


    html.Label('this is a range slider'),
    dcc.RangeSlider(
        min = 1,
        max = 10,
        step = .5,
        value = [3,7],
        marks = {i:i for i in range(10)}
    ),

    html.Br(),
    html.Br(),


    html.Label('This is a range slider'),
    html.Br(),
    html.Br(),
    dcc.Input(
        placeholder = 'Input your Name',
        type = 'text',
        value = ''
    ),

    html.Br(),
    
    html.Button('Submit',id = 'submit.form'),

    html.Br(),
    html.Br(),

    dcc.Textarea(
        placeholder = 'Input your Feedback',
        value = 'placeholder for text',
        style = {'width' : '100%'}
    ),

    html.Br(),
    html.Br(),

    dcc.Checklist(
         options = [
            {'label' : 'San Francisco', 'value' : 'SF'},
            {'label' : 'New York City', 'value'  : 'NYC'},
            {'label' : 'Santiago', 'value' : 'SCL'}
        ],
        values = ['SF','NYC']
    ),

    html.Br(),
    html.Br(),

    dcc.RadioItems(
        options = [
            {'label' : 'San Francisco', 'value' : 'SF'},
            {'label' : 'New York City', 'value'  : 'NYC'},
            {'label' : 'Santiago', 'value' : 'SCL'}
        ],
        value = 'SF'
    ),

    html.Br(),
    html.Br(),

   dcc.DatePickerSingle(
       id = 'dt-pick-single',
       date = dt(2015,5,10)
   ),

    html.Br(),
    html.Br(),

    dcc.DatePickerRange(
        id = 'dt-pick-range',
        start_date = dt(2015,5,10),
        end_date_placeholder_text = 'Select the end date'
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
