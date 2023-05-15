import dash
from dash import html, dcc
from src.callbacks import callbacks_control_panel
from src.layouts.layouts_common import get_title_section_layout, get_cloud_setting_layout
from src.layouts.layouts_control_panel import get_control_panel_contents_layout

dash.register_page(__name__, path='/')

layout = html.Div(
    id='div-control-panel',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Inspector Control Panel'),
        html.Br(),

        #####################
        #
        # Cloud Settings
        #
        #####################
        get_cloud_setting_layout(),
        html.Br(),

        #####################
        #
        # Contents
        #
        #####################
        html.Div(id='hidden-div-control-panel'),

        html.Div(
            id='control-panel-contents',
            children=get_control_panel_contents_layout(),
            # children=[
            #     html.Div(
            #         id='configs',
            #         children=[
            #             html.H4('Config Files'),
            #             dcc.RadioItems(
            #                 id='radioItems-configs',
            #                 options=[
            #                     'Config File Reader',
            #                 ],
            #                 value=None,
            #                 style={
            #                     'padding': 20,
            #                     'flex': 10
            #                 },  
            #             ),
            #         ],
            #         style={
            #             'width': '20%',
            #             'margin': '10px 10px 10px 10px'
            #         },
            #     ),
            #     html.Br(),

            #     html.Div(
            #         id='metadata',
            #         children=[
            #             html.H4('Meta Data'),
            #             dcc.RadioItems(
            #                 id='radioItems-metadata',
            #                 options=[
            #                     'Network Analyzer Layer',
            #                     'Model Layer'
            #                 ],
            #                 value=None,
            #                 style={
            #                     'padding': 20,
            #                     'flex': 10
            #                 },  
            #             ),
            #         ],
            #         style={
            #             'width': '20%',
            #             'margin': '10px 10px 10px 10px'
            #         },
            #     ),
            #     html.Br(),

            #     html.Div(
            #         id='simulation',
            #         children=[
            #             html.H4('Simulation'),
            #             dcc.RadioItems(
            #                 id='radioItems-simulation',
            #                 options=[
            #                     'AP&I',
            #                     'Traditional Supply Chain',
            #                     'Simulator'
            #                 ],
            #                 value=None,
            #                 style={
            #                     'padding': 20,
            #                     'flex': 10
            #                 }, 
            #             ),
            #         ],
            #         style={
            #             'width': '20%',
            #             'margin': '10px 10px 10px 10px'
            #         },
            #     ),
            #     html.Br(),

            #     html.Div(
            #         id='forecast',
            #         children=[
            #             html.H4('Forecast'),
            #             dcc.RadioItems(
            #                 id='radioItems-forecast',
            #                 options=[
            #                     'Order',
            #                     'Demand'
            #                 ],
            #                 value=None,
            #                 style={
            #                     'padding': 20,
            #                     'flex': 10
            #                 }, 
            #             ),
            #         ],
            #         style={
            #             'width': '20%',
            #             'margin': '10px 10px 10px 10px'
            #         },
            #     ),
            #     html.Br(),
            # ],
            # style={'display': 'flex'},
        ),
        html.Br(),
    ],
)


