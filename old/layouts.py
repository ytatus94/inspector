from datetime import date
from dash import dcc, html

def get_title_section_layout(page_name):
    layout = html.Div(
        id='page-title-section',
        children=[
            html.Div(
                children=[
                    html.H1(
                        id='page-title-control-panel',
                        children=page_name,
                        className='page-title',
                        style={
                            'font-weight': 'bold',
                            'text-align': 'left'
                        },
                    ),
                ],
                #style={'width': '80%', 'border-style': 'dotted'},
                style={'width': '80%'},
            ),

            html.Div(
                children=[
                    html.H1(
                        id='seeloz',
                        children='SEELOZ',
                        className='seeloz-logo',
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                            'text-align': 'right'
                        },
                    )
                ],
                #style={'width': '20%', 'border-style': 'dotted'},
                style={'width': '20%'},
            ),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_cloud_setting_layout():
    layout = html.Div(
        id='cloud-setting-section',
        children=[
            # Cloud Service
            html.Div(
                children=[
                    html.Label('Select Cloud Service:'),
                    dcc.Dropdown( 
                        id='dropdown-cloud-service',
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
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Project
            html.Div(
                children=[
                    html.Label('Select Project:'),
                    dcc.Dropdown( 
                        id='dropdown-project',
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
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Bucket
            html.Div(
                children=[
                    html.Label('Select Bucket:'),
                    dcc.Dropdown( 
                        id='dropdown-bucket',
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
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Customer Name
            html.Div(
                children=[
                    html.Label('Select Customer:'),
                    dcc.Dropdown( 
                        id='dropdown-customer-name',
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
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
        ],
        style={'display': 'flex'},
    )

    return layout

        # This is a dummy object used for callback no output
        # html.Div(
        #     id='hidden-div-1',
        #     style={'display': 'none'}
        # ),


def get_input_data_path_layout(default_path):
    layout = html.Div(
        id='input-path-section',
        children=[
            # text field
            html.Div(
                children=[
                    dcc.Input(
                        id='input-data-path',
                        type='text',
                        value=default_path,
                        style={'width': '100%'},
                    ),
                    
                ],
                style={'width': '63%', 'margin': '10px 10px 10px 10px'},
            ),
            # button
            html.Div(
                children=[
                    html.Button(
                        id='button-confirm',
                        n_clicks=0,
                        children='Confirm',
                        style={'width': '100%'},
                    ),
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_wid_pid_filter_layout(all_options):
    layout = html.Div(
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
    )

    return layout

def get_date_range_filter_layout(start_date, end_date):
    layout = html.Div(
        children=[
            html.Label(['Date range:']), 
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=start_date, 
                end_date=end_date, 
                display_format='YYYY-MM-Do'
            ),
        ],
        style={'width': '50%', 'margin': '10px 10px 10px 10px'},
    )

    return layout

def get_inventory_layout(dict_dfs):
    df_inventory = dict_dfs['inventory_levels']
    print(df_inventory.head())

    pairs = list(set(zip(df_inventory['warehouse_id'], df_inventory['product_id'])))
    print(len(pairs), pairs)

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    print(all_options)

    layout = html.Div(
        children=[
            html.Div(
                id='filter-section',
                children=[
                    get_wid_pid_filter_layout(all_options),
                    get_date_range_filter_layout(start_date='2021-06-01', end_date='2021-12-31')
                ],
                style={'display': 'flex'},
            ),
        ],
        
    )

    return layout


def get_demand_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_orders_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_deliveries_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_purchases_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_procurements_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_lead_time_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_stock_outs_layout(dict_dfs):
    layout = html.Div(

    )

    return layout


def get_safety_stock_layout(dict_dfs):
    layout = html.Div(

    )

    return layout



   
# Metadata
#list_of_tabs_network_analyzer = [
#    dcc.Tab(label='Inventory', value='tab_network_analyzer_layer_inventory'),
#    dcc.Tab(label='Demands', value='tab_network_analyzer_layer_demands'),
#    dcc.Tab(label='Orders', value='tab_network_analyzer_layer_orders'),
#    dcc.Tab(label='Deliveries', value='tab_network_analyzer_layer_deliveries'),
#    dcc.Tab(label='Purchases', value='tab_network_analyzer_layer_purchases'),
#    dcc.Tab(label='Procurements', value='tab_network_analyzer_layer_procurements'),
#    dcc.Tab(label='Lead Time', value='tab_network_analyzer_layer_lead_time'),
#    dcc.Tab(label='Stock Outs', value='tab_network_analyzer_layer_stock_outs'),
#    dcc.Tab(label='Safety Stock', value='tab_network_analyzer_layer_safety_stock'),
#]
#
#list_of_tabs_model = [
#    dcc.Tab(label='Inventory', value='tab_model_layer_inventory'),
#    dcc.Tab(label='Demands', value='tab_model_layer_demands'),
#    dcc.Tab(label='Orders', value='tab_model_layer_orders'),
#    dcc.Tab(label='Deliveries', value='tab_model_layer_deliveries'),
#    dcc.Tab(label='Purchases', value='tab_model_layer_purchases'),
#    dcc.Tab(label='Procurements', value='tab_model_layer_procurements'),
#    dcc.Tab(label='Lead Time', value='tab_model_layer_lead_time'),
#    dcc.Tab(label='Stock Outs', value='tab_model_layer_stock_outs'),
#    dcc.Tab(label='Safety Stock', value='tab_model_layer_safety_stock'),
#]
#
## Simulation
#list_of_tabs_apni = [
#    dcc.Tab(label='AP&I results', value='tab_apni_results'),
#    dcc.Tab(label='AP&I comparison', value='tab_apni_comparison'),
#]
#
#list_of_tabs_traditional = []
#
#list_of_tabs_simulator = [
#    dcc.Tab(label='AP&I Purchases', value='tab_simulator_results_apni_purchases'),
#    dcc.Tab(label='Daily Consumption', value='tab_simulator_results_daily_consumption'),
#    dcc.Tab(label='Daily Production', value='tab_simulator_results_daily_production'),
#    dcc.Tab(label='Deliveries', value='tab_simulator_results_deliveries'),
#    dcc.Tab(label='Inventory Levels', value='tab_simulator_results_inventory_levels'),
#    dcc.Tab(label='Lost Sales', value='tab_simulator_results_lost_sales'),
#    dcc.Tab(label='Orders', value='tab_simulator_results_orders'),
#    dcc.Tab(label='Procurements', value='tab_simulator_results_procurements'),
#    dcc.Tab(label='Production Orders', value='tab_simulator_results_production_orders'),
#    dcc.Tab(label='Purchases', value='tab_simulator_results_purchases'),
#    dcc.Tab(label='Resource Usage', value='tab_simulator_results_resource_usage'),
#    dcc.Tab(label='Sim Records', value='tab_simulator_results_sim_records'),
#]
#
## Forecast
#
##
#dropdown_wid = [
#    html.Label(['Warehousd ID:']),
#    dcc.Dropdown( 
#        id='dropdown_wid',
#        options=[
#            {'label': 'Total', 'value': 'tot'},
#            {'label': 'a warehouse', 'value': 'wid'},
#        ],
#        value='tot',
#        searchable=False,
#        clearable=False,
#    ),
#]
#
#dropdown_pid = [
#    html.Label(['Product ID:']),
#    dcc.Dropdown( 
#        id='dropdown_pid',
#        options=[
#            {'label': 'Total', 'value': 'tot'},
#            {'label': 'a product', 'value': 'pid'},
#        ],
#        value='tot',
#        searchable=False,
#        clearable=False,
#    ),
#]
#
#date_picker_range = [
#    html.Label(['Date range:']), 
#    dcc.DatePickerRange(
#        start_date=date(2021, 1, 1), 
#        end_date=date(2022, 12, 31), 
#        display_format='YYYY-MM-Do'
#    )
#]
#
#list_of_selector_objs = [
#    html.Div(children=dropdown_wid, style=dict(width='20%', marginRight='3em')),
#    html.Div(children=dropdown_pid, style=dict(width='20%', marginRight='3em')),
#    html.Div(children=date_picker_range, style=dict(width='50%')),
#]
#
#input_historical = [
#    dcc.Input(placeholder='Historical path', type='text', value=''),
#    html.Button('Load', id='button_load_historical'),
#]
#
#input_apni_ai = [
#    dcc.Input(placeholder='AI path', type='text', value=''),
#    html.Button('Load', id='button_load_apni_ai'),
#]
#
#input_apni_tr = [
#    dcc.Input(placeholder='Traditional path', type='text', value=''),
#    html.Button('Load', id='button_load_apni_tr'),
#]
#
#list_of_file_path_objs = [
#    html.Div(children=input_historical),
#    html.Div(children=input_apni_ai),
#    html.Div(children=input_apni_tr),
#]
