import pandas as pd                       #to perform data manipulation and analysis
import numpy as np    
import dash
from dash import dcc 
from dash import html
from dash.dependencies import Input, Output #to cleanse data
from datetime import datetime             #to manipulate dates
import plotly.express as px               #to create interactive charts
    

super_data = pd.read_excel("b2bsupercarryfor.xlsx")

app = dash.Dash(__name__)

#------------------------------------------------------------------------------------------------------------------

app.layout = html.Div([
    html.Div([
        html.Label(['2019 Concessional Carry forward']), 
        dcc.Dropdown(
            id='my_dropdown', 
            options=[
                {'label':'Surname', 'value': 'Client Last Name'}, 
                {'label': 'Age', 'value': 'Age'}, 
                {'label': 'TSB-18', 'value': 'Super Balance June 2018'}, 
                {'label': 'CCFYE18', 'value': 'Contributed amount 2018'}, 
                {'label': 'ANNCCMAX20', 'value': 'Max CC for 2019'}, 
                {'label': 'Avail19', 'value': 'Avail CC carryforward 2019'}, 
            ],
            value='Contributed amount 2018', 
            multi=False,
            clearable=False, 
            style={"width": "50%"}
        ),
    ]),
    
    html.Div([
        dcc.Graph(id= 'the_graph')
    ]), 
    
])

#------------------------------------------------------------------------------------

@app.callback( 
    Output(component_id='the_graph', component_property= 'figure'), 
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    dff = super_data
    
    piechart=px.pie(
        data_frame=dff, 
        names=my_dropdown, 
        hole=.2, 
        )
    return (piechart) 

if __name__ == '__main__':
    app.run_server(debug=True)

