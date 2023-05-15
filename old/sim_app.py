import os

import dash
from dash import Dash, html, dcc, Output, Input, State, callback

import plotly.express as px
import plotly.graph_objects as go

import webbrowser
from threading import Timer

from datetime import datetime, timedelta

from cloudio import CloudIO
from src.utils.data_handler import DataHandler

def open_browser():
    port = 8050
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(port))


dh = DataHandler(
    'azure',
    'seelozdevelop',
    'seeloz-ingress-prod',
    'ingress'
)

dict_df_simulator = dh.get_simulator_results('customers/ingress/simulation/latest/')
print(dict_df_simulator.keys())
print(dict_df_simulator['AI'].keys())
print(dict_df_simulator['TR'].keys())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
app.layout = html.Div(children=[
    html.H1(
        id='page-title-simulator-analysis',
        children='Simulator Analysis'
    ),
    html.Br(),

    # Cloud Service
    html.Label('Select Cloud Service:'),
    dcc.Dropdown( 
        id='dropdown-cloud-service-simulator-analysis',
        placeholder='Cloud',
        options=[
            {'label': 'Azure', 'value': 'Azure'},
            {'label': 'Google Cloud Platform', 'value': 'GCP'},
            {'label': 'Amazon AWS', 'value': 'S3'},
        ],
        value='Azure',
        searchable=False,
        clearable=False,
        multi=False,
    ),

    # Project
    html.Label('Select Project:'),
    dcc.Dropdown( 
        id='dropdown-project-simulator-analysis',
        placeholder='Project',
        options=[
            {'label': 'seelozdevelop', 'value': 'seelozdevelop'},
        ],
        value='seelozdevelop',
        searchable=False,
        clearable=False,
        multi=False,
    ),

    # Bucket
    html.Label('Select Bucket:'),
    dcc.Dropdown( 
        id='dropdown-bucket-simulator-analysis',
        placeholder='Bucket',
        options=[
            {'label': 'dev', 'value': 'dev'},
            {'label': 'prod', 'value': 'prod'},
            {'label': 'test', 'value': 'test'},
        ],
        value='dev',
        searchable=False,
        clearable=False,
        multi=False,
    ),

    # Customer Name
    html.Label('Select Customer:'),
    dcc.Dropdown( 
        id='dropdown-customer-name-simulator-analysis',
        placeholder='Customer Name',
        options=[
            {'label': 'Ingress', 'value': 'ingress'},
            {'label': 'Pactiv', 'value': 'pactiv'},
        ],
        value='ingress',
        searchable=False,
        clearable=False,
        multi=False,
    ),
    html.Br(),

    dcc.Input(
        id='input-simulator-results-path',
        type='text',
        value=f'customers/ingress/simulation/latest/',
    ),

    html.Button(id='submit-button-state-simulator-analysis', n_clicks=0, children='Submit'),
    html.Br(),

    html.Div(
        id='div-tabs-section-simulator-analysis',
        children=[
            dcc.Tabs(
                id='tabs-simulator-analysis',
                value='tab_simulator_sim_records',
                children=[
                    dcc.Tab(id='tab-simulator-apni-purchase', label='APNI Purchase', value='tab_simulator_apni_purchase'),
                    dcc.Tab(id='tab-simulator-daily-consumption', label='Daily Consumption', value='tab_simulator_daily_consumption'),
                    dcc.Tab(id='tab-simulator-daily_production', label='Daily Production', value='tab_simulator_daily_production'),
                    dcc.Tab(id='tab-simulator-deliveries', label='Deliveries', value='tab_simulator_deliveries'),
                    dcc.Tab(id='tab-simulator-inventory-levels', label='Inventory Levels', value='tab_simulator_inventory_levels'),
                    dcc.Tab(id='tab-simulator-lost-sales', label='Lost Sales', value='tab_simulator_lost_sales'),
                    dcc.Tab(id='tab-simulator-orders', label='Orders', value='tab_simulator_orders'),
                    dcc.Tab(id='tab-simulator-procurements', label='Procurements', value='tab_simulator_procurements'),
                    dcc.Tab(id='tab-simulator-production-orders', label='Production Orders', value='tab_simulator_production_orders'),
                    dcc.Tab(id='tab-simulator-purchases', label='Purchases', value='tab_simulator_purchases'),
                    dcc.Tab(id='tab-simulator-resource-usage', label='Resource Usage', value='tab_simulator_resource_usage'),
                    dcc.Tab(id='tab-simulator-sim-records', label='Sim Records', value='tab_simulator_sim_records'),
                ],
            ),
        ],
    ),
    html.Br(),

    html.Div(id='simulator-content')

])


@app.callback(
    Output('simulator-content', 'children'),
    Input('tabs-simulator-analysis', 'value')
)
def update_simulator_content(value):
    if value == 'tab_simulator_apni_purchase':
        df = dict_df_simulator['apni_purchase']
    elif value == 'tab_simulator_daily_consumption':
        df = dict_df_simulator['daily_consumption']
    elif value == 'tab_simulator_daily_production':
        df = dict_df_simulator['daily_production']
    elif value == 'tab_simulator_deliveries':
        df = dict_df_simulator['deliveries']
    elif value == 'tab_simulator_inventory_levels':
        df = dict_df_simulator['inventory_levels']
    elif value == 'tab_simulator_lost_sales':
        df = dict_df_simulator['lost_sales']
    elif value == 'tab_simulator_orders':
        df = dict_df_simulator['orders']
    elif value == 'tab_simulator_procurements':
        df = dict_df_simulator['procurements']
    elif value == 'tab_simulator_production_orders':
        df = dict_df_simulator['production_orders']
    elif value == 'tab_simulator_purchases':
        df = dict_df_simulator['purchases']
    elif value == 'tab_simulator_resource_usage':
        df = dict_df_simulator['resource_usage']
    elif value == 'tab_simulator_sim_records':
        print('in callback')
        print(dict_df_simulator.keys())
        print(dict_df_simulator['AI'].keys())
        df = dict_df_simulator['AI']['sim_records']
        print(df.head())

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    all_options = []
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    print(len(all_options))
    print(all_options)

 
    simulator_content_layout = html.Div(children=[
        html.Label(['(Warehousd ID, Product ID):']),
        dcc.Dropdown( 
            id='dropdown-pair',
            options=all_options,
            #value='(2401, 1218753076)',
            value=all_options[0]['value'],
            searchable=False,
            clearable=False,
            multi=False,
        ),

        html.Label(['Date range:']), 
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date='2021-06-01', 
            end_date='2021-12-31', 
            display_format='YYYY-MM-Do'
        ),


        dcc.Graph(id='graph-sim-records'),
        html.Div(id='table-sim-records'),
    ])

    return simulator_content_layout 

@app.callback(
    Output('graph-sim-records', 'figure'),
    Input('dropdown-pair', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    State('tabs-simulator-analysis', 'value'),
)
def update_figure(pair, start_date, end_date, value):
    print('call update_figure', pair, start_date, end_date, value) 
    if value == 'tab_simulator_apni_purchase':
        df = dict_df_simulator['apni_purchase']
    elif value == 'tab_simulator_daily_consumption':
        df = dict_df_simulator['daily_consumption']
    elif value == 'tab_simulator_daily_production':
        df = dict_df_simulator['daily_production']
    elif value == 'tab_simulator_deliveries':
        df = dict_df_simulator['deliveries']
    elif value == 'tab_simulator_inventory_levels':
        df = dict_df_simulator['inventory_levels']
    elif value == 'tab_simulator_lost_sales':
        df = dict_df_simulator['lost_sales']
    elif value == 'tab_simulator_orders':
        df = dict_df_simulator['orders']
    elif value == 'tab_simulator_procurements':
        df = dict_df_simulator['procurements']
    elif value == 'tab_simulator_production_orders':
        df = dict_df_simulator['production_orders']
    elif value == 'tab_simulator_purchases':
        df = dict_df_simulator['purchases']
    elif value == 'tab_simulator_resource_usage':
        df = dict_df_simulator['resource_usage']
    elif value == 'tab_simulator_sim_records':
        print('in callback')
        print(dict_df_simulator.keys())
        print(dict_df_simulator['AI'].keys())
        df = dict_df_simulator['AI']['sim_records']
        print(df.head())

    s = datetime.strptime(start_date, '%Y-%m-%d')
    e = datetime.strptime(end_date, '%Y-%m-%d')
    if pair is not None:
        wid = int(pair.split(',')[0].replace('(', ''))
        pid = int(pair.split(',')[1].replace(')', ''))
        print(wid, pid)
        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=s.strftime('%Y-%m-%d'))&
            (df['date']<=e.strftime('%Y-%m-%d'))
        ]
        print('in update_figures: the df_sub')
    else:
        print('in update_figures: df_sub=df')
        df_sub = df

    print(df_sub.head()) 

    fig_inv = px.bar(
        df_sub,
        x='date',
        y='inventory',
        title=f'inventory for ({wid}, {pid}) between {start_date} and {end_date}'
    )

    fig_inv.add_bar(x=df_sub['date'], y=df_sub['demand'], name="demand")
    fig_inv.add_bar(x=df_sub['date'], y=df_sub['procurement'], name="procurement")
    fig_inv.add_bar(x=df_sub['date'], y=df_sub['production'], name="production")
    fig_inv.add_bar(x=df_sub['date'], y=df_sub['waste'], name="waste")
    fig_inv.add_bar(x=df_sub['date'], y=df_sub['outgoing_warehouse_movements'], name="outgoing_warehouse_movements")
    fig_inv.add_bar(x=df_sub['date'], y=df_sub['incoming_warehouse_movements'], name="incoming_warehouse_movements")


    return fig_inv

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)
