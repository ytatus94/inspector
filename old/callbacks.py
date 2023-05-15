# import coloredlogs
# import json
# import logging
# import os
# from dash import html, dcc, callback, Input, Output, State
# from src.utils.data_handler import DataHandler
# from src.utils.get_logger import get_logger
# from cloudio import CloudIO


# logger = get_logger(enable_log=True)

# ##################################################
# #
# # callback functions for control_panel
# #
# ##################################################

# @callback(
#     Output(component_id='store-cloud-setting', component_property='data'),
#     Input(component_id='dropdown-cloud-service', component_property='value'),
#     Input(component_id='dropdown-project', component_property='value'),
#     Input(component_id='dropdown-bucket', component_property='value'),
#     Input(component_id='dropdown-customer-name', component_property='value')
# )
# def update_cloud_setting(
#         cloud_service,
#         project,
#         bucket,
#         customer_name
#     ):
#     logger.info('Call callback: update_cloud_setting()')
#     logger.info(f'\tcloud_service={cloud_service}, project={project}, bucket={bucket}, customer={customer_name}')

#     cloud_setting = {
#         'cloud_service': cloud_service,
#         'project': project,
#         'bucket': bucket,
#         'customer_name': customer_name,
#     }
#     logger.info(type(cloud_setting))
#     logger.info(cloud_setting)

#     return json.dumps(cloud_setting)


# @callback(
#     Output(component_id='hidden-div-2', component_property='children'),
#     Output(component_id='div-metadata', component_property='children'),
#     Output(component_id='div-simulation', component_property='children'),
#     Output(component_id='div-forecast', component_property='children'),
#     Input(component_id='radioItems-metadata', component_property='value'),
#     Input(component_id='radioItems-simulation', component_property='value'),
#     Input(component_id='radioItems-forecast', component_property='value'),
# )
# def open_analyzer(metadata_value, simulation_value, forecast_value):
#     logger.info('Call callback: open_analyzer()')

#     redirect_destination= None
#     # Meta Data
#     if metadata_value == 'Network Analyzer Layer':
#         logger.info(f'\tClick metadata {metadata_value}, open Network Analyzer layer')
#         redirect_destination = dcc.Location(
#             id='pages-metadata-network-analyzer-layer',
#             pathname='/metadata-network-analyzer-layer',
#         )
#     elif metadata_value == 'Model Layer':
#         logger.info(f'\tClick metadata {metadata_value}, open Model layer')
#         redirect_destination = dcc.Location(
#             id='pages-metadata-network-analyzer-layer',
#             pathname='/metadata-model-layer',
#         )

#     # Simulation
#     if simulation_value == 'AP&I':
#         logger.info(f'\tClick metadata {simulation_value}, open AP&I analyzer')
#         redirect_destination = dcc.Location(
#             id='pages-simulation-apni',
#             pathname='/simulation-apni',
#         )
#     elif simulation_value == 'Traditional Supply Chain':
#         logger.info(f'\tClick metadata {simulation_value}, open Traditional analyzer')
#         redirect_destination = dcc.Location(
#             id='pages-simulation-traditional',
#             pathname='/simulation-traditional',
#         )
#     elif simulation_value == 'Simulator':
#         logger.info(f'\tClick metadata {simulation_value}, open Simulator analyzer')
#         redirect_destination = dcc.Location(
#             id='pages-simulation-simulator',
#             pathname='/simulation-simulator',
#         )

#     # Forecast
#     if forecast_value == 'Order':
#         logger.info(f'\tClick metadata {forecast_value}, open order forecast')
#         redirect_destination = dcc.Location(
#             id='pages-forecast-order',
#             pathname='/forecast-order',
#         )
#     elif forecast_value == 'Demand':
#         logger.info(f'\tClick metadata {forecast_value}, open order forecast')
#         redirect_destination = dcc.Location(
#             id='pages-forecast-demand',
#             pathname='/forecast-demand',
#         )

#     # Reset radio items
#     # Because metadata, simulation, and forecast sections are independent,
#     # We have to avoid users select an item in each section. We only allow
#     # one item to be selected
#     metadata_children=[
#         html.Label(children='Meta Data'),
#         dcc.RadioItems(
#             id='radioItems-metadata',
#             options=['Network Analyzer Layer', 'Model Layer'],
#             value=None,
#             style={'padding': 20, 'flex': 10},  
#         ),
#     ]

#     simulation_children=[
#         html.Label('Simulation'),
#         dcc.RadioItems(
#             id='radioItems-simulation',
#             options=['AP&I', 'Traditional Supply Chain', 'Simulator'],
#             value=None,
#             style={'padding': 20, 'flex': 10},
#         ),
#     ]
    
#     forecast_children=[
#         html.Label(['Forecast']),
#         dcc.RadioItems(
#             id='radioItems-forecast',
#             options=['Order', 'Demand'],
#             value=None,
#             style={'padding': 20, 'flex': 10},
#         ),
#     ]

#     return redirect_destination, metadata_children, simulation_children, forecast_children


##################################################
#
# callback functions for metadata_network_analyzer_layer
#
##################################################

# @callback(
#     Output(component_id='', component_property=''),
#     Input(component_id='', component_property='value'),
# )
# def function(value):
#     pass


# ##################################################
# #
# # callback functions for metadata_model_layer
# #
# ##################################################

# @callback(
#     #Output(component_id='metadata-model-layer-dataframe', component_property='data'),
#     Output(component_id='cloud-setting-metadata-model-layer', component_property='children'),
#     Input(component_id='store-cloud-setting', component_property='data'),
# )
# def load_data_for_model_layer_analysis(jsonified_cloud_setting):
#     logger.info('Call callback: load_data_for_model_layer_analysis()')

#     cloud_setting = json.loads(jsonified_cloud_setting)
    
#     cloud_service=cloud_setting['cloud_service']
#     project=cloud_setting['project']
#     bucket=cloud_setting['bucket']
#     customer_name = cloud_setting['customer_name']

#     cloud_setting_children=[
#         html.Table(
#             html.Tr([
#                 html.Td(['Cloud Service:', cloud_service]),
#                 html.Td(['Project:', project]),
#                 html.Td(['Bucket:', bucket]),
#                 html.Td(['Customer:', customer_name]),
#                 html.Td(['Model layer:', f'customers/{customer_name}/model/']),
#             ]),
#         ),
#     ]

# #    dh = DataHandler(
# #        cloud_service,
# #        project,
# #        bucket,
# #        customer_name
# #    )
# #    dict_df_metadata = dh.get_metadata('model')

# #    json_df_metadata = dict()
# #    for table_name in dict_df_metadata.keys():
# #        json_df = dict_df_metadata[table_name].to_json(date_format='iso', orient='split')
# #        json_df_metadata[table_name] = json_df

#     return cloud_setting_children


# # @callback(
# #     Output(component_id='', component_property=''),
# #     Input(component_id='metadata-model-layer-dataframe', component_property='data'),
# # )
# # def update_model_layer_graph(value):
# #     logger.info('Call callback: update_model_layer_graph')
# #     pass

# #     dff = pd.read_json(jsonified_cleaned_data, orient='split')

##################################################
#
# callback functions for simulation_apni
#
##################################################

@callback(
    Output(component_id='cloud-setting-simulation-apni', component_property='children'),
    Input(component_id='store-cloud-setting', component_property='data'),
)
def update_dropdown_apni_analysis(jsonified_cloud_setting):
    logger.info('Call callback: update_dropdown_apni_analysis()')

    cloud_setting = json.loads(jsonified_cloud_setting)
    
    cloud_service=cloud_setting['cloud_service']
    project=cloud_setting['project']
    bucket=cloud_setting['bucket']
    customer_name = cloud_setting['customer_name']

    cloud_setting_children=[
        # Cloud Service
        html.Label('Select Cloud Service:'),
        dcc.Dropdown( 
            id='dropdown-cloud-service-apni-analysis',
            placeholder='Cloud',
            options=[
                {'label': 'Azure', 'value': 'Azure'},
                {'label': 'Google Cloud Platform', 'value': 'GCP'},
                {'label': 'Amazon AWS', 'value': 'S3'},
            ],
            value=cloud_service,
            searchable=False,
            clearable=False,
            multi=False,
        ),

        # Project
        html.Label('Select Project:'),
        dcc.Dropdown( 
            id='dropdown-project-apni-analysis',
            placeholder='Project',
            options=[
                {'label': 'seelozdevelop', 'value': 'seelozdevelop'},
            ],
            value=project,
            searchable=False,
            clearable=False,
            multi=False,
        ),

        # Bucket
        html.Label('Select Bucket:'),
        dcc.Dropdown( 
            id='dropdown-bucket-apni-analysis',
            placeholder='Bucket',
            options=[
                {'label': 'dev', 'value': 'dev'},
                {'label': 'prod', 'value': 'prod'},
                {'label': 'test', 'value': 'test'},
            ],
            value=bucket,
            searchable=False,
            clearable=False,
            multi=False,
        ),

        # Customer Name
        html.Label('Select Customer:'),
        dcc.Dropdown( 
            id='dropdown-customer-name-apni-analysis',
            placeholder='Customer Name',
            options=[
                {'label': 'Ingress', 'value': 'ingress'},
                {'label': 'Pactiv', 'value': 'pactiv'},
            ],
            value=customer_name,
            searchable=False,
            clearable=False,
            multi=False,
        ),

        dcc.Input(
            id='input-apni-results-path-apni-analysis',
            type='text',
            value=f'customers/{customer_name}/apni/singlewarehouse/results/latest/',
        ),

        html.Button(id='submit-button-state-apni-analysis', n_clicks=0, children='Submit'),
    ]

    return cloud_setting_children

@callback(
    Output(component_id='df-apni-results-ai', component_property='data'),
    Output(component_id='df-apni-results-tr', component_property='data'),
    Input(component_id='submit-button-state-apni-analysis', component_property='n_clicks'),
    State(component_id='dropdown-cloud-service-apni-analysis', component_property='value'),
    State(component_id='dropdown-project-apni-analysis', component_property='value'),
    State(component_id='dropdown-bucket-apni-analysis', component_property='value'),
    State(component_id='dropdown-customer-name-apni-analysis', component_property='value'),
    State(component_id='input-apni-results-path-apni-analysis', component_property='value'),
)
def load_data_for_apni_analysis(n_clicks, cloud_service, project, bucket, customer_name, apni_results_path):
    logger.info('Call callback: load_data_for_apni_analysis()')
    logger.info(f'\tLoad data from {cloud_service}:{project}/{bucket}/{apni_results_path}')

#    dh = DataHandler(
#        cloud_service,
#        project,
#        bucket,
#        customer_name
#    )
#    print("starting to load apni results...")
#    dict_df_apni = dh.get_apni_results(apni_results_path)

#    print(dict_df_apni['AI'].head())
#    print(dict_df_apni['TR'].head())

#    json_df_apni_ai = dict_df_apni['AI'].to_json(date_format='iso', orient='split')
#    json_df_apni_tr = dict_df_apni['TR'].to_json(date_format='iso', orient='split')

    client = CloudIO(
        cloud_service,
        project,
        bucket,
    )

    json_df_apni_ai = None
    json_df_apni_tr = None
        
    return json_df_apni_ai, json_df_apni_tr

##################################################
#
# callback functions for simulation_simulator
#
##################################################

# @callback(
#     Output(component_id='', component_property=''),
#     Input(component_id='', component_property='value'),
# )
# def function(value):
#     pass


##################################################
#
# callback functions for simulation_traditional
#
##################################################

# @callback(
#     Output(component_id='', component_property=''),
#     Input(component_id='', component_property='value'),
# )
# def function(value):
#     pass


##################################################
#
# callback functions for forecast_demand
#
##################################################

# @callback(
#     Output(component_id='', component_property=''),
#     Input(component_id='', component_property='value'),
# )
# def function(value):
#     pass


##################################################
#
# callback functions for forecast_order
#
##################################################

# @callback(
#     Output(component_id='', component_property=''),
#     Input(component_id='', component_property='value'),
# )
# def function(value):
#     pass







# @callback(
#     Output('graph-model-layer', 'figure'),
#     Input('dropdown-pair', 'value'),
#     Input('date-picker-range', 'start_date'),
#     Input('date-picker-range', 'end_date'),
# )
# def plot_model_layer(pair, start_date, end_date):
#     if pair is not None:
#         wid = int(pair.split(',')[0].lstrip('('))
#         pid = int(pair.split(',')[-1].rstrip(')'))

#     if start_date is not None:
#         start_date_object = date.fromisoformat(start_date)
#         start_date_string = start_date_object.strftime('%Y-%m-%d')

#     if end_date is not None:
#         end_date_object = date.fromisoformat(end_date)
#         end_date_string = end_date_object.strftime('%Y-%m-%d')
        
#     print(f'Current pair={pair}, (wid, pid)=({wid}, {pid}), start_date={start_date}, start_date_string={start_date_string}, end_date={end_date}, end_date_string={end_date_string}')

#     # df_inventory_level = self.dict_df_model_layer['inventory_levels']
#     # df_sub = df_inventory_level.loc[
#     #     (df_inventory_level['warehouse_id']==wid) &
#     #     (df_inventory_level['product_id']==pid) &
#     #     (df_inventory_level['date']>=start_date) &
#     #     (df_inventory_level['date']<=end_date)
#     # ]
#     # print(df_sub.head())

#     fig = None
#     return fig


# @app.callback(
#     Output(component_id='my-output', component_property='children'),
#     Input(component_id='RadioItems-metadata', component_property='value')
# )
# def select_RadioItems_metadata_network_analyzer_layer()


# @app.callback(
#     Output('model_layer_plot', 'figure'),
#     Input('tabs_tables', 'value')
# )
# def update_graph(tab_value):
#     if tab_value == 'tab_inventory':
#         fig = plot_inventory_levels()
#     elif tab_value == 'tab_demands':
#         fig = plot_demands()
#     elif tab_value == 'tab_orders':
#         fig = plot_orders()
#     elif tab_value == 'tab_deliveries':
#         fig = plot_deilveries()
#     elif tab_value == 'tab_purchases':
#         fig = plot_purchases()
#     elif tab_value == 'tab_procurements':
#         fig = plot_procurements()
#     elif tab_value == 'tab_lead_time':
#         fig = plot_lead_time()
#     elif tab_value == 'tab_stock_outs':
#         fig = plt_stock_outs()
#     elif tab_value == 'tab_safety_stock':
#         fig = plt_safety_stock()

#     # map_tab_values_and_table_names = {
#     #     'tab_inventory': 'inventory_levels',
#     #     'tab_demands': [
#     #         'daily_demand_from_orders', 
#     #         'daily_demand_from_deliveries',
#     #         'monthly_demand_from_orders',
#     #         'monthly_demand_from_deliveries',
#     #     ],
#     #     'tab_orders': 'orders',
#     #     'tab_deliveries': 'deliveries',
#     #     'tab_purchases': 'purchases',
#     #     'tab_procurements': 'procurements',
#     #     'tab_lead_time': 'lead_time',
#     #     'tab_stock_outs': 'stock_outs',
#     #     'tab_safety_stock': 'safety_stock'
#     # }

#     # table_name = map_tab_values_and_table_names.get(tab_value)


#     # # df_table = tuple_of_dfs[table_name]
#     # df_table = tuple_of_dfs['inventory_levels']
#     # print(df_table.head())

#     # if 'date' in df_table.columns:
#     #     df_table['date'] = pd.to_datetime(df_table['date'], infer_datetime_format=True)

#     # fig = px.line(df_table, x='date', y='quantity')

#     return fig
