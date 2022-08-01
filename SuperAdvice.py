import pandas as pd  # to perform data manipulation and analysis
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output  # to cleanse data
from datetime import datetime  # to manipulate dates
import plotly.express as px  # to create interactive charts

super_data = pd.read_excel("b2bsupercarryfor.xlsx")

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------------------------------------------

app.layout = html.Div(
    [
        html.Div(
            [
                html.Label(["2019 Concessional Carry forward"]),
                dcc.Dropdown(
                    id="my_dropdown",
                    options=[
                        {"label": "Client Last Name", "value": "Surname"},
                        {"label": "Age", "value": "Age"},
                        {"label": "Super Balance June 2018", "value": "TSB-18"},
                        {"label": "Contributed amount 2018", "value": "CCFYE18"},
                        {"label": "Max CC for 2019", "value": "ANNCCMAX20"},
                        {"label": "Avail CC carryforward 2019", "value": "Avail19"},
                    ],
                    value="CCFYE18",
                    multi=False,
                    clearable=False,
                    style={"width": "50%"},
                ),
            ]
        ),
        html.Div([dcc.Graph(id="the_graph")]),
    ]
)


# ------------------------------------------------------------------------------------


@app.callback(
    Output(component_id="the_graph", component_property="figure"),
    [Input(component_id="my_dropdown", component_property="value")],
)
def update_graph(my_dropdown):
    dff = super_data

    piechart = px.pie(data_frame=dff, names=my_dropdown, hole=0.2, )
    return piechart


if __name__ == "__main__":
    app.run_server(debug=True)
