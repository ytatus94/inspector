import dash
from dash import html, dcc
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-network-analyzer-layer',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Network Analyzer Layer Analysis'),
        html.Br(),

        #####################
        # 
        # Input data
        #
        #####################
        html.Div(id='current-cloud-setting'),
        html.Br(),

        #####################
        # 
        # Tabs
        #
        #####################
        html.Div(
            id='tabs-section',
            children=[
                dcc.Tabs(
                    id='tabs-network-analyzer-layer',
                    value='tab_network_analyzer_layer_inventory',
                    children=[
                        dcc.Tab(
                            id='tab-inventory',
                            label='Inventory',
                            value='tab_network_analyzer_layer_inventory',
                        ),
                        dcc.Tab(
                            id='tab-demands',
                            label='Demands',
                            value='tab_network_analyzer_layer_demands',
                        ),
                        dcc.Tab(
                            id='tab-orders',
                            label='Orders',
                            value='tab_network_analyzer_layer_orders',
                        ),
                        dcc.Tab(
                            id='tab-deliveries',
                            label='Deliveries',
                            value='tab_network_analyzer_layer_deliveries',
                        ),
                        dcc.Tab(
                            id='tab-purchases',
                            label='Purchases',
                            value='tab_network_analyzer_layer_purchases',
                        ),
                        dcc.Tab(
                            id='tab-procurements',
                            label='Procurements',
                            value='tab_network_analyzer_layer_procurements',
                        ),
                        dcc.Tab(
                            id='tab-lead-time',
                            label='Lead Time',
                            value='tab_network_analyzer_layer_lead_time',
                        ),
                        dcc.Tab(
                            id='tab-stock-outs', 
                            label='Stock Outs',
                            value='tab_network_analyzer_layer_stock_outs',
                        ),
                        dcc.Tab(
                            id='tab-safety-stock',
                            label='Safety Stock',
                            value='tab_network_analyzer_layer_safety_stock',
                        ),
                    ],
                ),
            ],
        ),
        html.Br(),

        #####################
        #
        # Contents
        #
        #####################
        html.Div(id='hidden-div-network-analyzer-layer'),

        html.Div(id='metadata-network-analyzer-layer-filters'),

        html.Div(
            children=[
                html.H4('Time Series Distribution:'),
                dcc.Graph(id='metadata-network-analyzer-layer-figure'),
            ],
        ),
        html.Br(),

        html.Div(
            children=[
                html.H4('Statistics:'),
                html.Div(id='metadata-network-analyzer-layer-statistics'),
            ],
        ),
        html.Br(),

        html.H2(children='Not support yet'),
        html.Br(),
    ],
)


