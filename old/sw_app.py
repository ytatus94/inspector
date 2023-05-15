import os

import dash
from dash import Dash, html, dcc, Output, Input, State, callback
#import dash_bootstrap_components as dbc


import plotly.express as px
import plotly.graph_objects as go

import webbrowser
from threading import Timer

from datetime import datetime, timedelta

from cloudio import CloudIO
from src.utils.data_handler import DataHandler

import json

def open_browser():
    port = 8050
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(port))


dh = DataHandler(
    'azure',
    'seelozdevelop',
    'seeloz-ingress-dev',
    'ingress'
)

print('Load apni results...')
dict_df_apni = dh.get_apni_results('customers/ingress/apni/singlewarehouse/results/latest/')
print(dict_df_apni['AI'].head())
print(dict_df_apni['TR'].head())


pairs = list(set(zip(dict_df_apni['AI']['warehouse_id'], dict_df_apni['TR']['product_id'])))
all_options = [{'label': 'all', 'value': 'all'}]
for wid, pid in pairs:
    all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
print(all_options)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
app.layout = html.Div(children=[
    #####################
    #
    # Title
    #
    #####################
    html.Div(
        id='page-title-section',
        children=[
            html.Div(
                children=[
                    html.H1(
                        id='seeloz',
                        children='SEELOZ',
                        className='seeloz-logo',
                        style={'font-family': 'Sans-serif', 'font-weight': 'bold', 'color': 'Tomato'},
                    ),
                ],
                style={'width': '20%', 'border-style': 'dotted'},
            ),

            html.Div(
                children=[
                    html.H1(
                        id='page-title-simulation-apni',
                        children='AP&I Analysis',
                        className='page-title',
                        style={'font-weight': 'bold', 'text-align': 'center'},
                    ),
                ],
                style={'width': '80%', 'border-style': 'dotted'},
            ),
        ],
        style={'display': 'flex'},
    ),
    html.Br(),


    #####################
    #
    # Cloud Settings
    #
    #####################
    html.Div(
        id='cloud-setting-section',
        children=[
            # Cloud Service
            html.Div(
                children=[
                    html.Label('Select Cloud Service:'),
                    dcc.Dropdown( 
                        id='dropdown-cloud-service-apni-analysis',
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
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),

            # Project
            html.Div(
                children=[
                    html.Label('Select Project:'),
                    dcc.Dropdown( 
                        id='dropdown-project-apni-analysis',
                        placeholder='Project',
                        options=[
                            {'label': 'seelozdevelop', 'value': 'seelozdevelop'},
                        ],
                        value='seelozdevelop',
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),

            # Bucket
            html.Div(
                children=[
                    html.Label('Select Bucket:'),
                    dcc.Dropdown( 
                        id='dropdown-bucket-apni-analysis',
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
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),

            # Customer Name
            html.Div(
                children=[
                    html.Label('Select Customer:'),
                    dcc.Dropdown( 
                        id='dropdown-customer-name-apni-analysis',
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
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),
        ],
        style={'display': 'flex'},
    ),

    html.Div(
        id='input-path-section',
        children=[
            # text field
            html.Div(
                children=[
                    dcc.Input(
                        id='input-apni-results-path-apni-analysis',
                        type='text',
                        value=f'customers/ingress/apni/singlewarehouse/results/latest/',
                        style={'width': '100%'},
                    ),
                    
                ],
                style={'width': '63%', 'margin': '10px 10px 10px 10px'},
            ),
            # button
            html.Div(
                children=[
                    html.Button(
                        id='button-submit-apni-analysis',
                        n_clicks=0,
                        children='Confirm',
                        style={'width': '100%'},
                    ),
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),
        ],
        style={'display': 'flex'},
    ),

    dcc.Store(id='intermediate-cloud-setting'),
    dcc.Store(id='intermediate-apni-dataframe'),


    #####################
    #
    # Tabs
    #
    #####################
    html.Div(
        id='tabs-section',
        children=[
            dcc.Tabs(
                id='tabs-apni-analysis',
                value='tab_singlewarehouse_results',
                children=[
                    dcc.Tab(
                        id='tab-singlewarehouse-results',
                        label='Results',
                        value='tab_singlewarehouse_results'
                    ),
                    dcc.Tab(
                        id='tab-singlewarehouse-comparisons',
                        label='Comparisons',
                        value='tab_singlewarehouse_comparisons'
                    ),
                ],
            ),
        ],
    ),
    html.Br(),

    #####################
    #
    # Analysis
    #
    #####################
    html.Div(
        id='filter-section',
        children=[
            html.Div(
                children=[
                    html.Label(['(Warehousd ID, Product ID):']),
                    dcc.Dropdown( 
                        id='dropdown-pair',
                        options=all_options,
                        value=all_options[0]['value'],
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),

            html.Div(
                children=[
                    html.Label(['Date range:']), 
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date='2021-06-01', 
                        end_date='2021-12-31', 
                        display_format='YYYY-MM-Do'
                    ),
                ],
                style={'width': '50%', 'margin': '10px 10px 10px 10px'},
            ),
        ],
        style={'display': 'flex'},
    ),

    html.Div(
        id='content-section',
        children=[
            html.Div(id='content-apni-results')
        ]
    )


    #html.Div(
    #    id='plot-section',
    #    children=[
    #        dcc.Graph(id='graph-apni-results'),
    #    ],
    #),
    #html.Br(),

    #html.Div(
    #    id='summary-section',
    #    children=[
    #        html.Div(
    #            children=[
    #                html.H4('Single Warehouse Results:'),
    #                html.Div(id='summary-dataframe'),
    #            ],
    #        ),
    #        #html.Div(id='summary'),
    #    ],
    #)
    #html.Br()
])



@app.callback(
    Output('intermediate-cloud-setting', 'data'),
    Input('button-submit-apni-analysis', 'n_clicks'),
    State('dropdown-cloud-service-apni-analysis', 'value'),
    State('dropdown-project-apni-analysis', 'value'),
    State('dropdown-bucket-apni-analysis', 'value'),
    State('dropdown-customer-name-apni-analysis', 'value'),
    State('input-apni-results-path-apni-analysis', 'value'),
)
def update_cloud_setting(n_clicks, cloud_service, project, bucket, customer_name, apni_results_path):
    print('call update_cloud_setting', n_clicks, cloud_service, project, bucket, customer_name, apni_results_path)
    json_cloud_setting = {
        'cloud_service': cloud_service,
        'project': project,
        'bucket': bucket,
        'customer_name': customer_name,
        'apni_results_path': apni_results_path
    }
    return json.dumps(json_cloud_setting)

@app.callback(
    Output('intermediate-apni-dataframe', 'data'),
    Input('intermediate-cloud-setting', 'data'),
)
def update_data(cloud_setting):
    print('call update_data', cloud_setting)
    print(type(cloud_setting))
    json_cloud_setting = json.loads(cloud_setting)
    print(type(json_cloud_setting))
    print(json_cloud_setting)
    

    print('instantiate client...')
    client = CloudIO(
        json_cloud_setting['cloud_service'],
        json_cloud_setting['project'],
        json_cloud_setting['bucket']
    )
    print('finish instantiate client...')

    print('instantiate dh obj...')
    dh_obj = DataHandler(
        json_cloud_setting['cloud_service'],
        json_cloud_setting['project'],
        json_cloud_setting['bucket'],
        json_cloud_setting['customer_name']
    )
    print('finish instantiate dh obj')

    return json.dump(json_cloud_setting)



def plot_results(df, title):
    figure = px.line(
        df,
        x='date',
        y='inventory',
        title=title,
    )

    figure.add_bar(
        x=df['date'],
        y=df['demand'],
        name='Demand',
    )

    figure.add_bar(
        x=df['date'],
        y=df['sales'],
        name='Sales',
    )

    figure.add_bar(
        x=df['date'],
        y=df['purchase'],
        name='Purchase',
    )

    figure.add_bar(
        x=df['date'],
        y=df['procurement'],
        name='Procurement',
    )

    figure.add_bar(
        x=df['date'],
        y=df['lostsales'],
        name='Lost Sales',
    )

    figure.update_layout(hovermode='x unified')

    return figure

#def generate_table(df)
#    children = html.Table([
#        html.Thead(
#            html.Tr([html.Th(col) for col in df.columns])
#        ),

#        html.Tbody([
#            html.Tr([
#                html.Td(df.iloc[i][col]) for col in df.columns
#            ]) for i in range(min(len(dataframe), max_rows))
#        ])
#    ])

#    return children

@app.callback(
    Output('apni-results', 'figure'),
    Input('dropdown-pair', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
)
def update_results(pair, start_date, end_date):
    print('call update_figures:', pair, start_date, end_date)

    df = dict_df_apni['AI'].copy()

    if pair == 'all':
        df_all = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date)
            ]
            .groupby('date')
            .agg({
                'inventory': 'sum',
                'demand': 'sum',
                'sales': 'sum',
                'purchase': 'sum',
                'procurement': 'sum',
                'lostsales': 'sum',
            })
            .reset_index()
        )

        print('use df_all:')
        print(df_all.head())
        figure = plot_results(
            df=df_all,
            title=f'Single warehouse results for all (warehouse_id, product_id) between {start_date} and {end_date}'
        )
    else:
        wid = int(pair.split(',')[0].replace('(', ''))
        pid = int(pair.split(',')[1].replace(')', ''))
        print(wid, pid)
        
        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
        print('use df_sub:')
        print(df_sub.head())

        figure = plot_results(
            df=df_sub,
            title=f'Single warehouse results for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure

@app.callback(
    Output('content-apni-results', 'children'),
    Input('tabs-apni-analysis', 'value'),
)
def update_analysis_content(value):
    print('call update_analysis_content', value)
    children = []
    if value == 'tab_singlewarehouse_results':
        print('render results')
        children = [
            html.Div(
                id='plot-section',
                children=[
                    dcc.Graph(id='graph-apni-results'),
                ],
            ),
            html.Br(),

            html.Div(
                id='summary-section',
                children=[
                    html.Div(
                        children=[
                            html.H4('Single Warehouse Results:'),
                            html.Div(id='summary-dataframe'),
                        ],
                    ),
                    #html.Div(id='summary'),
                ],
            ),
            html.Br()
        ]
    elif value == 'tab_singlewarehouse_comparisons':
        print('render comparison')
        children = [
            html.Div(
                html.H4('Under construction...')
            ),
            html.Br()
        ]

    return children

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)
