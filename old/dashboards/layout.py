# import dash
# from dash import Dash, dcc, html, callback, Input, Output, State
# import src.dashboards as db
# from datetime import date
# from cloudio import CloudIO
# from src.utils.data_handler import DataHandler
# import plotly.express as px
# import pandas as pd

# class DashboardLayout:
#     def __init__(self, args):
#         pass
#     #     self.dashboard = dashboard
#         # self.data_handler = DataHandler(args)
#         # self.dict_df_model_layer = None

#     def get_layout(self):
#         return self.get_control_panel_layout()
#         # if self.dashboard == 'model':
#         #     print('Use model dashboard')
#         #     return self.get_model_layer_layout()
#         # elif self.dashboard == 'apni':
#         #     print('Use apni dashboard')
#         #     return self.get_apni_layout()
#         # elif self.dashboard == 'simulator':
#         #     print('Use simulator dashboard')
#         #     return self.get_simulator_layout()
#         # elif self.dashboard == 'forecast':
#         #     print('Use forecast dashboard')
#         #     return self.get_forecast_layout()

#     def get_control_panel_layout(self):
#         control_panel = html.Div(
#             children=[
#                 # represents the browser address bar and doesn't render anything
#                 # dcc.Location(id='url', refresh=False),
                
#                 html.H1('Inspector Control Panel', id='inspector_control_panel'),
                
#                 html.Div(
#                     children=[
#                         # Cloud Service
#                         html.Label('Select Cloud Service:'),
#                         dcc.Dropdown( 
#                             id='dropdown-cloud-service',
#                             placeholder='Cloud',
#                             options=[
#                                 {'label': 'Azure', 'value': 'Azure'},
#                                 {'label': 'Google Cloud Platform', 'value': 'GCP'},
#                                 {'label': 'Amazon AWS', 'value': 'S3'},
#                             ],
#                             value='Azure',
#                             searchable=False,
#                             clearable=False,
#                             multi=False,
#                         ),

#                         # Project
#                         html.Label('Select Project:'),
#                         dcc.Dropdown( 
#                             id='dropdown-project',
#                             placeholder='Project',
#                             options=[
#                                 {'label': 'seelozdevelop', 'value': 'seelozdevelop'},
#                             ],
#                             value='seelozdevelop',
#                             searchable=False,
#                             clearable=False,
#                             multi=False,
#                         ),

#                         # Bucket
#                         html.Label('Select Bucket:'),
#                         dcc.Dropdown( 
#                             id='dropdown-bucket',
#                             placeholder='Bucket',
#                             options=[
#                                 {'label': 'dev', 'value': 'dev'},
#                                 {'label': 'prod', 'value': 'prod'},
#                                 {'label': 'test', 'value': 'test'},
#                             ],
#                             value='prod',
#                             searchable=False,
#                             clearable=False,
#                             multi=False,
#                         ),

#                         # Customer Name
#                         html.Label('Select Customer:'),
#                         dcc.Dropdown( 
#                             id='dropdown-customer-name',
#                             placeholder='Select bucket',
#                             options=[
#                                 {'label': 'Ingress', 'value': 'ingress'},
#                                 {'label': 'Pactiv', 'value': 'pactiv'},
#                             ],
#                             value='ingress',
#                             searchable=False,
#                             clearable=False,
#                             multi=False,
#                         ),
#                     ],
#                 ),
#                 html.Br(),

#                 html.Div(
#                     children=[
#                         html.Div(
#                             children=[
#                                 html.Label('Meta Data'),
#                                 dcc.RadioItems(
#                                     ['Network Analyzer Layer', 'Model Layer'],
#                                     style={'padding': 20, 'flex': 10},
#                                     id='RadioItems-metadata',
#                                 ),
#                             ],
#                         ),
#                         html.Br(),

#                         html.Div(
#                             children=[
#                                 html.Label('Simulation'),
#                                 dcc.RadioItems(
#                                     ['AP&I', 'Traditional', 'Simulator'],
#                                     style={'padding': 20, 'flex': 10},
#                                     id='RadioItems-simulation'
#                                 ),
#                             ],
#                         ),
#                         html.Br(),

#                         html.Div(
#                             children=[
#                                 html.Label(['Forecast']),
#                                 dcc.RadioItems(
#                                     ['Order', 'Demand'],
#                                     style={'padding': 20, 'flex': 10},
#                                     id='RadioItems-forecast',
#                                 ),
#                             ],
#                         ),
#                         html.Br(),
#                     ],
#                 ),
#                 html.Br(),

#                 html.Div(
#                     [
#                         html.Div(
#                             dcc.Link(
#                                 f"{page['name']} - {page['path']}", href=page["relative_path"]
#                             )
#                         )
#                         for page in dash.page_registry.values()
#                     ],
#                 ),
#                 dash.page_container,

#                 # html.Label(['start multipages']),
#                 # html.Div(
#                 #     children=[
#                 #         dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
#                 #         for page in dash.page_registry.values()
#                 #     ]
#                 # ),
#                 # html.Label(['End multipages']),
#                 # dash.page_container
#             ],
#         )
#         return control_panel

#     def get_network_analyzer_layer_layout(self):
#         network_analyzer_layer_object = html.Div(
#             children=[
#                 html.H1(children='Network Analyzer Layer Analysis'),
#             ]
#         )
#         return network_analyzer_layer_object

#     def get_model_layer_layout(self, args):
#         # client = CloudIO(
#         #     args.cloud_service,
#         #     args.project,
#         #     args.bucket
#         # )
#         # all_tables = client.list_dir('customers/ingress/model/')
#         # print(all_tables)

#         # data_tables = [
#         #     'inventory_levels',
#         #     'monthly_demand_from_orders',
#         #     'monthly_demand_from_deliveries',
#         #     'daily_demand_from_orders',
#         #     'daily_demand_from_deliveries',
#         #     'orders',
#         #     'deliveries',
#         #     'purchases',
#         #     'procurements',
#         #     'lead_time',
#         #     'stock_outs',
#         #     'safety_stock',
#         # ]
#         # print('Loading data...')
#         # datasets = client.load_parallel(
#         #     [f'customers/ingress/model/{table}' for table in data_tables],
#         #     logger=None
#         # )
#         # print('Finish loading data...')

#         #  # Unpack 'datasets'
#         # (
#         #     df_inventory_level,
#         #     df_mdo, # monthly_demand_from_orders
#         #     df_mdd, # monthly_demand_from_deliveries
#         #     df_ddo, # daily_demand_from_orders
#         #     df_ddd, # daily_demand_from_deliveries
#         #     df_orders,
#         #     df_deliveries,
#         #     df_purchases,
#         #     df_procurements,
#         #     df_lead_time,
#         #     df_stock_outs,
#         #     df_safety_stock,
#         # ) = datasets
#         # self.dict_df_model_layer = self.data_handler.get_metadata('model')
#         # df_inventory_level = self.dict_df_model_layer['inventory_levels']


#         # all_pairs = list(set(zip(df_inventory_level['warehouse_id'], df_inventory_level['product_id'])))
#         # # print(len(all_pairs))
#         # # print(all_pairs)

#         # list_option_pairs = []
#         # for pair in all_pairs:
#         #     label = f'({pair[0]}, {pair[1]})'
#         #     list_option_pairs.append({'label': label, 'value': label})
#         # print(len(list_option_pairs))
#         # # print(list_option_pairs)

#         model_layer_layout_obj = html.Div(
#             children=[
#                 # Title section
#                 html.H1('Model Layer Analysis', id='page_title'),
#                 html.Br(),
#                 # dcc.Tabs(id='tabs_tables', value='tab_inventory', children=db.list_of_tabs_model),
#                 # html.Div(id='selectors', children=db.list_of_selector_objs, style=dict(display='flex', marginTop='3em')),
#                 # html.Div(id='plot_inventory', children=[dcc.Graph(id='model_layer_plot')]),

#                 # Tabs section
#                 html.Div(
#                     children=[
#                         dcc.Tabs(
#                             id='tabs-model-layer',
#                             value='tab_model_layer_inventory',
#                             children=[
#                                 dcc.Tab(id='tab-inventory', label='Inventory', value='tab_model_layer_inventory'),
#                                 dcc.Tab(id='tab-demands', label='Demands', value='tab_model_layer_demands'),
#                                 dcc.Tab(id='tab-orders', label='Orders', value='tab_model_layer_orders'),
#                                 dcc.Tab(id='tab-deliveries', label='Deliveries', value='tab_model_layer_deliveries'),
#                                 dcc.Tab(id='tab-purchases', label='Purchases', value='tab_model_layer_purchases'),
#                                 dcc.Tab(id='tab-procurements', label='Procurements', value='tab_model_layer_procurements'),
#                                 dcc.Tab(id='tab-lead-time', label='Lead Time', value='tab_model_layer_lead_time'),
#                                 dcc.Tab(id='tab-stock-outs', label='Stock Outs', value='tab_model_layer_stock_outs'),
#                                 dcc.Tab(id='tab-safety-stock', label='Safety Stock', value='tab_model_layer_safety_stock'),
#                             ]
#                         )
#                     ]
#                 ),
#                 html.Br(),

#                 # Plot section
#                 html.Div(
#                     id='tabs-model-layer-content',
#                     children=[
#                         html.Div(html.H3('Hahaha'))
#                     ]
#                 ),
#                 html.Br(),

#                 # # Selector section
#                 # html.Div(
#                 #     children=[
#                 #         html.Label(['(Warehousd ID, Product ID):']),
#                 #         dcc.Dropdown( 
#                 #             id='dropdown-pair',
#                 #             options=[
#                 #                 {'label': 'Total', 'value': 'tot'},
#                 #                 {'label': 'a warehouse', 'value': 'wid'},
#                 #             ],
#                 #             value='tot',
#                 #             # options=list_option_pairs,
#                 #             # value=list_option_pairs[0]['value'],
#                 #             searchable=False,
#                 #             clearable=False,
#                 #         ),
#                 #     ],
#                 # ),
#                 # html.Br(),

#                 # html.Div(
#                 #     children=[
#                 #         html.Label(['Date range:']), 
#                 #         dcc.DatePickerRange(
#                 #             id='date-picker-range',
#                 #             start_date=date(2021, 1, 1), 
#                 #             end_date=date(2022, 12, 31), 
#                 #             display_format='YYYY-MM-Do'
#                 #         ),
#                 #     ]
#                 # ),
#                 # html.Br(),

#                 # # Plot section
#                 # html.Div(
#                 #     children=[
#                 #         dcc.Graph(id='graph-model-layer'),
#                 #     ]
#                 # ),
#                 # html.Br(),
#             ],
#         )
#         # print(type(model_layout_obj))
#         return model_layer_layout_obj


#     def get_apni_layout(self):
#         apni_layout_obj = html.Div(
#             children=[
#                 # Title
#                 html.H1('APNI Analysis'),
#                 html.Br(),

#                 # html.Div(
#                 #     children=[
#                 #         'AP&I Results Path:',
#                 #         dcc.Input(id='input-apni-results-path', type='text', value='customers/ingress/apni/singlewarehouse/results/latest/'),
#                 #         html.Button(id='load-apni-results', n_clicks=0, children='Load'),
#                 #     ]
#                 # ),
#                 # html.Br(),

#                 # Tabs
#                 html.Div(
#                     children=[
#                         # dcc.Tabs(id='tabs-apni', value='tab_apni', children=db.list_of_tabs_apni),
#                         dcc.Tabs(
#                             children=[
#                                 dcc.Tab(label='AP&I results', value='tab_apni_results'),
#                                 dcc.Tab(label='AP&I comparison', value='tab_apni_comparison'),
#                             ],
#                             id='tabs-apni',
#                             value='tab_apni',
#                         ),
#                     ],
#                 ),
#                 html.Br(),

#                 # html.Div(id='input-path', children=db.list_of_file_path_objs),
#                 # html.Div(id='selectors', children=db.list_of_selector_objs, style=dict(display='flex', marginTop='3em')),

#                 # Data path
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children=[
#                                 'Historical Path',
#                                 dcc.Input(
#                                     placeholder='Historical path',
#                                     type='text',
#                                     value='customers/ingress/model/inventory_levels/',
#                                     id='historical-path',
#                                 ),
#                             ],
#                         ),

#                         html.Div(
#                             children=[
#                                 'AP&I path',
#                                 dcc.Input(
#                                     placeholder='AP&I path',
#                                     type='text',
#                                     value='customers/ingress/apni/singlewarehouse/results/latest/',
#                                     id='aphi-path'
#                                 ),
#                             ],
#                         ),

#                         html.Div(
#                             children=[
#                                 html.Button('Load', id='button-load-apni'),
#                             ],
#                         ),
#                     ]
#                 ),
#                 html.Br(),

#                 # Widgets
#                 html.Div(
#                     children=[
#                         html.Div(
#                             children=[
#                                 html.Label(['Warehousd ID:']),
#                                 dcc.Dropdown( 
#                                     id='dropdown-wid',
#                                     options=[
#                                         {'label': 'Total', 'value': 'tot'},
#                                         {'label': 'a warehouse', 'value': 'wid'},
#                                     ],
#                                     value='tot',
#                                     searchable=False,
#                                     clearable=False,
#                                 ),
#                             ],
#                         ),

#                         html.Div(
#                             children=[
#                                 html.Label(['Product ID:']),
#                                 dcc.Dropdown( 
#                                     id='dropdown-pid',
#                                     options=[
#                                         {'label': 'Total', 'value': 'tot'},
#                                         {'label': 'a product', 'value': 'pid'},
#                                     ],
#                                     value='tot',
#                                     searchable=False,
#                                     clearable=False,
#                                 ),
#                             ],
#                         ),

#                         html.Div(
#                             children=[
#                                 html.Label(['Date range:']), 
#                                 dcc.DatePickerRange(
#                                     start_date=date(2021, 1, 1), 
#                                     end_date=date(2022, 12, 31), 
#                                     display_format='YYYY-MM-Do',
#                                 ),
#                             ],
#                         ),
#                     ],
#                 ),
#                 html.Br(),

#                 # Plot
#                 html.Div(
#                     children=[

#                     ],
#                 ),
#             ],
#         )

#         return apni_layout_obj

#     def get_traditional_layout(self):
#         traditional_layout_obj = html.Div(
#             children=[
#                 html.H1(children='Traditional Analysis')
#             ]
#         )
#         return traditional_layout_obj

#     def get_simulator_layout(self):
#         simulator_layout_obj = html.Div(
#             children=[
#                 html.H1(children='Simulator Analysis'),

#                 html.Div(
#                     children=[
#                         'Simulator Results Path:',
#                         dcc.Input(id='input-1-state', type='text', value='customers/ingress/simulation/latest/AI/'),
#                         html.Button(id='load-simulator-results', n_clicks=0, children='Load'),
#                     ]
#                 ),
#                 html.Br(),

#                 html.Div(
#                     children=[
#                         dcc.Tabs(id='tab-simulator-results', value='tab_simulator_results', children=db.list_of_tabs_simulator),
#                     ]
#                 ),

#                 html.Div(
#                     children=[
                        
#                     ]
#                 ),

#             ]
#         )
#         return simulator_layout_obj

#     def get_forecast_order_layout(self):
#         forecast_order_layout_obj = html.Div(
#             children=[
#                 html.H1(children='Forecasted Order Analysis')
#             ]
#         )
#         return forecast_order_layout_obj

#     def get_forecast_demand_layout(self):
#         forecast_demand_layout_obj = html.Div(
#             children=[
#                 html.H1(children='Forecasted Demand Analysis')
#             ]
#         )
#         return forecast_demand_layout_obj

#     # Meta Data
#     # @app.callback(
#     #     Output()
#     #     Input()
#     # )
#     # def get_model_layout():
#     @callback(
#         Output('tabs-model-layer-content', 'children'),
#         Input('tabs-model-layer', 'value'),
#     )
#     def render_content(tab):
#         '''
#         After clicking tab, render content
#         '''

#         # Load data
#         data_handler = DataHandler('azure', 'seelozdevelop', 'seeloz-ingress-prod')
#         dict_df_model_layer = data_handler.get_metadata('model')

#         if tab == 'tab_model_layer_inventory':
#             df = dict_df_model_layer['inventory_levels']
#             all_pairs = data_handler.get_all_wid_pid_pairs(df)
#             list_of_option_pairs = data_handler.get_list_of_options(all_pairs)
#             layout_model_layer_inventory =  html.Div(
#                 id='layout-model-layer-inventory',
#                 children=[
#                     # Selector section
#                     html.Label(['(Warehousd ID, Product ID):']),
#                     dcc.Dropdown( 
#                         id='dropdown-pair',
#                         options=[
#                             {'label': 'Total', 'value': 'tot'},
#                             {'label': 'a warehouse', 'value': 'wid'},
#                         ],
#                         value='tot',
#                         # options=list_option_pairs,
#                         # value=list_option_pairs[0]['value'],
#                         searchable=False,
#                         clearable=False,
#                     ),
#                     html.Br(),

#                     html.Label(['Date range:']), 
#                     dcc.DatePickerRange(
#                         id='date-picker-range',
#                         start_date=date(2021, 1, 1), 
#                         end_date=date(2022, 12, 31), 
#                         display_format='YYYY-MM-Do'
#                     ),
#                     html.Br(),

#                     # Plot section
#                     # dcc.Graph(id='graph-model-layer-inventory'),
#                     # html.Br()

#                 ],
#             )
#         elif tab == 'tab_model_layer_demands':
#             return html.Div(html.H3("Tab demand is clicked, plot demand"))
#         elif tab == 'tab_model_layer_orders':
#             return html.Div(html.H3("Tab Orders is clicked, plot orders"))
#         elif tab == 'tab_model_layer_deliveries':
#             return html.Div(html.H3("Tab deliveries is clicked, plot delivery"))
#         elif tab == 'tab_model_layer_purchases':
#             return html.Div(html.H3("Tab purchases is clicked, plot purchases"))
#         elif tab == 'tab_model_layer_procurements':
#             return html.Div(html.H3("Tab procurements is clicked, plot procurements"))
#         elif tab == 'tab_model_layer_lead_time':
#             return html.Div(html.H3("Tab lead time is clicked, plot lead time"))
#         elif tab == 'tab_model_layer_stock_outs':
#             return html.Div(html.H3("Tab stock outs is clicked, plot stock outs"))
#         elif tab == 'tab_model_layer_safety_stock':
#             return html.Div(html.H3("Tab safety stock is clicked, plot safety stock"))

#     # @callback(
#     #     Output('graph-model-layer', 'figure'),
#     #     Input('tabs-model-layer', 'value'),
#     #     Input('tab-demands', 'value'),
#     #     Input('tab-orders', 'value'),
#     #     Input('tab-deliveries', 'value'),
#     #     Input('tab-purchases', 'value'),
#     #     Input('tab-procurements', 'value'),
#     #     Input('tab-lead-time', 'value'),
#     #     Input('tab-stock-outs', 'value'),
#     #     Input('tab-safety-stock', 'value'),
#     #     Input('dropdown-pair', 'value'),
#     #     Input('date-picker-range', 'start_date'),
#     #     Input('date-picker-range', 'end_date'),
#     # )
#     # def plot_model_layer(
#     #     tab,
#     #     pair, start_date, end_date):

#     #     data_handler = DataHandler(args)

#     #     self.dict_df_model_layer = self.data_handler.get_metadata('model')
#     #     df_inventory_level = self.dict_df_model_layer['inventory_levels']


#     #     all_pairs = list(set(zip(df_inventory_level['warehouse_id'], df_inventory_level['product_id'])))
#     #     # print(len(all_pairs))
#     #     # print(all_pairs)

#     #     list_option_pairs = []
#     #     for pair in all_pairs:
#     #         label = f'({pair[0]}, {pair[1]})'
#     #         list_option_pairs.append({'label': label, 'value': label})
#     #     print(len(list_option_pairs))
#     #     # print(list_option_pairs)


#         # if click_tab_inventory is not None:
#         #     print("Tab inventory is clicked, plot inventory level")
#         # elif click_tab_demand is not None:
#         #     print("Tab demand is clicked, plot demand")
#         # elif click_tab_orders is not None:
#         #     print("Tab Orders is clicked, plot orders")
#         # elif click_tab_deliveries is not None:
#         #     print("Tab deliveries is clicked, plot delivery")
#         # elif click_tab_purchases is not None:
#         #     print("Tab purchases is clicked, plot purchases")
#         # elif click_tab_procurements is not None:
#         #     print("Tab procurements is clicked, plot procurements")
#         # elif click_tab_lead_time is not None:
#         #     print("Tab lead time is clicked, plot lead time")
#         # elif click_tab_stock_outs is not None:
#         #     print("Tab stock outs is clicked, plot stock outs")
#         # elif click_tab_safety_stock is not None:
#         #     print("Tab safety stock is clicked, plot safety stock")

#         # if pair is not None:
#         #     wid = int(pair.split(',')[0].lstrip('('))
#         #     pid = int(pair.split(',')[-1].rstrip(')'))

#         # if start_date is not None:
#         #     start_date_object = date.fromisoformat(start_date)
#         #     start_date_string = start_date_object.strftime('%Y-%m-%d')

#         # if end_date is not None:
#         #     end_date_object = date.fromisoformat(end_date)
#         #     end_date_string = end_date_object.strftime('%Y-%m-%d')
            
#         # print(f'Current pair={pair}, (wid, pid)=({wid}, {pid}), start_date={start_date}, start_date_string={start_date_string}, end_date={end_date}, end_date_string={end_date_string}')

#         # df_inventory_level = self.dict_df_model_layer['inventory_levels']
#         # df_sub = df_inventory_level.loc[
#         #     (df_inventory_level['warehouse_id']==wid) &
#         #     (df_inventory_level['product_id']==pid) &
#         #     (df_inventory_level['date']>=start_date) &
#         #     (df_inventory_level['date']<=end_date)
#         # ]
#         # print(df_sub.head())


#         # df = pd.DataFrame({"x-title": [1,2,3,4,5], "y": [3, 9, 20, 15, 7]})
#         # fig = px.line(df, x="x-title", y="y-title", title='dummy plot')

#         # return fig

        

#     #     fig = px.line(
#     #         df_sub,
#     #         x='date',
#     #         y="lifeExp", title='Life expectancy in Canada')
#     #     fig.show()

#     #     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#     #                  size="pop", color="continent", hover_name="country",
#     #                  log_x=True, size_max=55)

#     # fig.update_layout(transition_duration=500)

#     # return fig



#     # @callback(
#     #     Output('output-state', 'children'),
#     #     Input('button-load-apni', 'n_clicks'),
#     #     State('historical-path', 'value'),
#     #     State('aphi-path', 'value')
#     # )
#     # def load_apni_data(n_clicks, input1, input2):
#     #     client = CloudIO('azure', 'seelozdevelop', 'seeloz-ingress-prod')
#     #     print(f'input1={input1}')
#     #     print(f'input2={input2}')

