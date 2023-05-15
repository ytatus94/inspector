import dash
from dash import html
from src.callbacks import callbacks_config_reader
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-config-reader',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Config File Reader'),
        html.Br(),

        #####################
        # 
        # Input data
        #
        #####################
        html.Div(id='current-cloud-setting'),
        html.Div(id='config-dir-path'),
        html.Br(),

        #####################
        #
        # Contents
        #
        #####################
        html.Div(id='hidden-div-config-reader'),

        html.Div(id='config-reader-contents'),
        html.Br(),
    ],
)


