import dash
from dash import html, dcc
from src.callbacks import callbacks_simulation_simulator
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-simulator',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Simulator Analysis'),
        html.Br(),

        #####################
        # 
        # Input data
        #
        #####################
        html.Div(id='current-cloud-setting'),
        html.Div(id='simulator-data-path'),
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
                    id='tabs-simulation-simulator',
                    value='tab_simulator_sim_records',
                    children=[
                        dcc.Tab(
                            id='tab-simulator-sim-records',
                            label='Sim Records',
                            value='tab_simulator_sim_records',
                        ),
                        # dcc.Tab(
                        #     id='tab-simulator-inventory-levels',
                        #     label='Inventory Levels',
                        #     value='tab_simulator_inventory_levels',
                        # ),
                        # dcc.Tab(
                        #     id='tab-simulator-purchases',
                        #     label='Purchases',
                        #     value='tab_simulator_purchases',
                        # ),
                        dcc.Tab(
                            id='tab-simulator-apni-purchases',
                            label='AP&I Purchases',
                            value='tab_simulator_apni_purchases',
                        ),
                        # dcc.Tab(
                        #     id='tab-simulator-procurements',
                        #     label='Procurements',
                        #     value='tab_simulator_procurements',
                        # ),
                        dcc.Tab(
                            id='tab-simulator-orders',
                            label='Orders',
                            value='tab_simulator_orders',
                        ),
                        # dcc.Tab(
                        #     id='tab-simulator-production-orders',
                        #     label='Production Orders',
                        #     value='tab_simulator_production_orders',
                        # ),
                        # dcc.Tab(
                        #     id='tab-simulator-deliveries',
                        #     label='Deliveries',
                        #     value='tab_simulator_deliveries',
                        # ),
                        # dcc.Tab(
                        #     id='tab-simulator-daily-production',
                        #     label='Daily Production',
                        #     value='tab_simulator_daily_production',
                        # ),
                        # dcc.Tab(
                        #     id='tab-simulator-daily-consumption',
                        #     label='Daily Consumption',
                        #     value='tab_simulator_daily_consumption',
                        # ),
                        dcc.Tab(
                            id='tab-simulator-lost-sales',
                            label='Lost Sales',
                            value='tab_simulator_lost_sales',
                        ),
                        dcc.Tab(
                            id='tab-simulator-resource-usage',
                            label='Resource Usage',
                            value='tab_simulator_resource_usage',
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
        html.Div(id='hidden-div-simulation-simulator'),

        html.Div(id='simulation-simulator-contents'),
 
        html.H2(children='Not support yet'),
        html.Br(),
    ],
)


