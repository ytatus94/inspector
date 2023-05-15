import json
from dash import html, dcc, callback, Input, Output, State
from src.utils.cloud_setting import create_all_DataHandler_objects
from src.utils.get_logger import get_logger


logger = get_logger(enable_log=True)

dict_dh_objects = create_all_DataHandler_objects()

##################################################
#
# callback functions for common parts
#
##################################################


@callback(
    Output(component_id='current-cloud-setting', component_property='children'),
    Input(component_id='store-cloud-setting', component_property='data'),
)
def show_current_cloud_setting(cloud_setting):
    logger.info(f'Call show_current_cloud_setting(): argument={cloud_setting}, type={type(cloud_setting)}')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')

    layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.H6('Current Cloud Setting:'),
                ],
                style={
                    'width': '20%',
                    'text-align': 'left',
                    'display': 'flex',
                },
            ),

            html.Div(
                children=[
                    html.H6('Cloud Service:'),
                    html.H6(
                        children=[
                            cloud_setting['cloud_service'],
                        ],
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                        },
                    ),
                ],
                style={
                    'width': '20%',
                    'text-align': 'left',
                    'display': 'flex',
                },
            ),

            html.Div(
                children=[
                    html.H6('Project:'),
                    html.H6(
                        children=[
                            cloud_setting['project'],
                        ],
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                        },
                    ),
                ],
                style={
                    'width': '20%',
                    'text-align': 'left',
                    'display': 'flex'
                },
            ),

            html.Div(
                children=[
                    html.H6('Bucket:'),
                    html.H6(
                        children=[
                            cloud_setting['bucket'],
                        ],
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                        },
                    ),
                ],
                style={
                    'width': '20%',
                    'text-align': 'left',
                    'display': 'flex'
                },
            ),

            html.Div(
                children=[
                    html.H6('Customer:'),
                    html.H6(
                        children=[
                            cloud_setting['customer_name'],
                        ],
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                        },
                    ),
                ],
                style={
                    'width': '20%',
                    'text-align': 'left',
                    'display': 'flex'
                },
            ),
        ],
        style={'display': 'flex'}
    )

    return layout


