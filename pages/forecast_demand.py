import dash
from dash import html
from src.layouts.layouts_common import get_title_section_layout


dash.register_page(__name__)

layout = html.Div(
    id='div-forecast-demand',
    children=[
        #####################
        #
        # Title
        #
        #####################
        get_title_section_layout('Demand Forecast Analysis'),
        html.Br(),

        html.H2(children='Not support yet'),
        html.Br(),
    ],
)


