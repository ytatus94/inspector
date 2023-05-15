import dash
from dash import html, dcc
from src.callbacks import callbacks_simulation_apni
# from src.layouts.layouts_common import get_title_section_layout, get_wid_pid_filter_layout, get_date_range_filter_layout
from src.layouts.layouts_common import get_title_section_layout
from src.layouts.layouts_apni import get_apni_results_contents


dash.register_page(__name__)

layout = html.Div(
    id='div-simulation-apni',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('AP&I Analysis'),
        html.Br(),

        #####################
        # 
        # Input data
        #
        #####################
        html.Div(id='current-cloud-setting'),
        html.Div(id='singlewarehouse-data-path'),
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
                    id='tabs-simulation-apni',
                    value='tab_singlewarehouse_results',
                    children=[
                        dcc.Tab(
                            id='tab-singlewarehouse-results',
                            label='Results',
                            value='tab_singlewarehouse_results',
                        ),
                        dcc.Tab(
                            id='tab-singlewarehouse-comparisons',
                            label='Comparisons',
                            value='tab_singlewarehouse_comparisons',
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
        html.Div(id='hidden-div-simulation-apni'),

        html.Div(
            id='simulation-apni-contents',
            children=[
                get_apni_results_contents(),
            ],
        ),

        # html.Div(
        #     id='simulation-apni-filters',
        #     children=[
        #         get_wid_pid_filter_layout([
        #             {'label': 'all', 'value': 'all'},
        #         ]),
        #         get_date_range_filter_layout(
        #             start_date='2021-01-01',
        #             end_date='2021-12-31'
        #         )
        #     ]
        # ),

        # html.Div(
        #     children=[
        #         html.H4('Time Series Distribution:'),
        #         dcc.Graph(id='simulation-apni-figure'),
        #     ],
        # ),
        # html.Br(),

        # html.Div(
        #     children=[
        #         html.H4('Statistics:'),
        #         html.Div(id='simulation-apni-statistics'),
        #     ],
        # ),
        # html.Br(),

        # html.Div(
        #     children=[
        #         html.H4('Table:'),
        #         html.Div(id='simulation-apni-table'),
        #     ],
        # ),
        # html.Br(),
    ],
)


