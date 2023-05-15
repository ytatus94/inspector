import dash
from dash import html, dcc
from src.callbacks import callbacks_simulation_traditional
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-traditional',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Traditional Supply Chain Analysis'),
        html.Br(),

        #####################
        # 
        # Input data
        #
        #####################
        html.Div(id='current-cloud-setting'),
        html.Div(id='traditional-supply-chain-path'),

        html.H2(children='Not support yet'),
        html.Br(),
    ],
)


