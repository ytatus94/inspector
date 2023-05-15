import dash_renderjson
import json
from dash import html, dcc, callback, Input, Output, State
from src.layouts.layouts_common import get_wid_pid_filter_layout, get_historical_data_path_layout, get_input_data_path_layout
from src.callbacks.callbacks_common import logger, dict_dh_objects
from src.utils.cloud_setting import get_DataHandler_object


##################################################
#
# callback functions for simulation AP&I
#
##################################################


@callback(
    Output(component_id='simulator-data-path', component_property='children'),
    Input(component_id='store-cloud-setting', component_property='data'),
)
def update_input_data_path(cloud_setting):
    logger.info(f'Call update_input_data_path():')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')

    customer_name = cloud_setting['customer_name']
    historical_data_path = f'customers/{customer_name}/model/'
    logger.info(f'\tCurrent historical_data_path={historical_data_path}')
    input_data_path = f'customers/{customer_name}/simulation/latest/'
    logger.info(f'\tCurrent input_data_path={input_data_path}')

    layout = html.Div(
        children=[
            get_historical_data_path_layout(historical_data_path),
            get_input_data_path_layout('Simulator Results Path:', input_data_path),
        ],
    )

    return layout


