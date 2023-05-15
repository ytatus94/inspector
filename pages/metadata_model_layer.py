import dash
from dash import html, dcc
from src.callbacks import callbacks_metadata_model_layer
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-model-layer',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Model Layer Analysis'),
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
                    id='tabs-model-layer',
                    value='tab_model_layer_inventory',
                    children=[
                        dcc.Tab(
                            id='tab-inventory',
                            label='Inventory',
                            value='tab_model_layer_inventory',
                        ),
                        dcc.Tab(
                            id='tab-demands',
                            label='Demands',
                            value='tab_model_layer_demands',
                        ),
                        dcc.Tab(
                            id='tab-orders',
                            label='Orders',
                            value='tab_model_layer_orders',
                        ),
                        dcc.Tab(
                            id='tab-deliveries',
                            label='Deliveries',
                            value='tab_model_layer_deliveries',
                        ),
                        dcc.Tab(
                            id='tab-purchases',
                            label='Purchases',
                            value='tab_model_layer_purchases',
                        ),
                        dcc.Tab(
                            id='tab-procurements',
                            label='Procurements',
                            value='tab_model_layer_procurements',
                        ),
                        dcc.Tab(
                            id='tab-lead-time',
                            label='Lead Time',
                            value='tab_model_layer_lead_time',
                        ),
                        dcc.Tab(
                            id='tab-stock-outs', 
                            label='Stock Outs',
                            value='tab_model_layer_stock_outs',
                        ),
                        dcc.Tab(
                            id='tab-safety-stock',
                            label='Safety Stock',
                            value='tab_model_layer_safety_stock',
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
        html.Div(id='hidden-div-model-layer'),

        html.Div(id='metadata-model-layer-filters'),

        html.Div(
            children=[
                html.H4('Time Series Distribution:'),
                dcc.Graph(id='metadata-model-layer-figure'),
            ],
        ),
        html.Br(),

        html.Div(
            children=[
                html.H4('Statistics:'),
                html.Div(id='metadata-model-layer-statistics'),
            ],
        ),
        html.Br(),

        # Because showing table in the dashboard takes a lot resource
        # and reduce the performance, I decide not to show table.
        # html.Div(
        #     children=[
        #         html.H4('Table:'),
        #         html.Div(id='metadata-model-layer-table'),
        #     ],
        # ),
        # html.Br(),
    ],
)


