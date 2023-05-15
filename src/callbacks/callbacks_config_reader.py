import dash_renderjson
import json
from dash import html, dcc, callback, Input, Output, State
from src.layouts.layouts_common import get_wid_pid_filter_layout, get_input_data_path_layout
from src.callbacks.callbacks_common import logger, dict_dh_objects
from src.utils.cloud_setting import get_DataHandler_object


##################################################
#
# callback functions for config reader
#
##################################################


@callback(
    Output(component_id='config-dir-path', component_property='children'),
    Input(component_id='store-cloud-setting', component_property='data'),
)
def update_input_data_path(cloud_setting):
    logger.info(f'Call update_config_reader_content():')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')

    customer_name = cloud_setting['customer_name']
    input_data_path = f'customers/{customer_name}/apni/singlewarehouse/configs/'
    logger.info(f'\tCurrent input_data_path={input_data_path}')

    return get_input_data_path_layout(
        title='Configs Path:',
        default_path=input_data_path,
        input_id='input-data-path',
        button_id='button-confirm'
    )


@callback(
    Output(component_id='config-reader-contents', component_property='children'),
    Input(component_id='button-confirm', component_property='n_clicks'),
    State(component_id='input-data-path', component_property='value'),
    State(component_id='store-cloud-setting', component_property='data'),
)
def update_config_reader_content(n_clicks, configs_folder_path, cloud_setting):
    logger.info(f'Call update_config_reader_content(): {configs_folder_path}')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')
    
    dh_object = get_DataHandler_object(
        dict_dh_objects=dict_dh_objects,
        cloud_service=cloud_setting['cloud_service'],
        project=cloud_setting['project'],
        bucket=cloud_setting['bucket'],
        customer_name=cloud_setting['customer_name'],
    )

    all_config_files = dh_object._client.list_blobs(configs_folder_path)
    logger.info(f'\tNumber of blobs in {configs_folder_path} are {len(all_config_files)}')

    if len(all_config_files) > 0:
        all_pairs = []
        all_options = []
        for config_file in all_config_files:
            if not config_file.endswith('json'):
                continue
            config_file = config_file.split('/')[-1]
            wid = int(config_file.split('_')[1])
            pid = int(config_file.split('_')[2].replace('.json', ''))
            all_pairs.append((wid, pid))
            all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})

        logger.info(f'\tNumber of pairs={len(all_pairs)}, Number of options={len(all_options)}')

        layout = html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4(f'Number of config files: {len(all_config_files)}')
                    ],
                    style={
                        'font-weight': 'bold',
                        'text-align': 'left'
                    },     
                ),

                html.Div(
                    id='filter-section',
                    children=[
                        get_wid_pid_filter_layout(all_options),
                    ],
                    style={'display': 'flex'},
                ),
                html.Br(),

                html.Div(
                    id='config-file-json',
                ),
                html.Br(),
            ],
        )
    else:
        layout = html.Div(
            children=[
                html.Div(
                    children=[
                        html.H4(f'Number of config files: {len(all_config_files)}')
                    ],
                    style={
                        'font-weight': 'bold',
                        'text-align': 'left'
                    },     
                ),
            ],
        )

    return layout

@callback(
    Output(component_id='config-file-json', component_property='children'),
    Input(component_id='dropdown-pair', component_property='value'),
    State(component_id='input-data-path', component_property='value'),
    State(component_id='store-cloud-setting', component_property='data'),
)
def update_config_file_json(selected_pair, configs_folder_path, cloud_setting):
    logger.info(f'Call update_config_file_json(): {selected_pair}')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')
    
    dh_object = get_DataHandler_object(
        dict_dh_objects=dict_dh_objects,
        cloud_service=cloud_setting['cloud_service'],
        project=cloud_setting['project'],
        bucket=cloud_setting['bucket'],
        customer_name=cloud_setting['customer_name'],
    )

    wid = int(selected_pair.split(',')[0].replace('(', ''))
    pid = int(selected_pair.split(',')[1].replace(')', ''))

    logger.info(f'\tLoad {configs_folder_path}config_{wid}_{pid}.json...')
    config_dict = dh_object._client.get_json(f'{configs_folder_path}config_{wid}_{pid}.json')

    theme = {
        'scheme': 'monokai',
        'author': 'wimer hazenberg (http://www.monokai.nl)',
        'base00': '#272822',
        'base01': '#383830',
        'base02': '#49483e',
        'base03': '#75715e',
        'base04': '#a59f85',
        'base05': '#f8f8f2',
        'base06': '#f5f4f1',
        'base07': '#f9f8f5',
        'base08': '#f92672',
        'base09': '#fd971f',
        'base0A': '#f4bf75',
        'base0B': '#a6e22e',
        'base0C': '#a1efe4',
        'base0D': '#66d9ef',
        'base0E': '#ae81ff',
        'base0F': '#cc6633',
    }

    layout = dash_renderjson.DashRenderjson(
        id='render-config-file-json',
        data=config_dict,
        max_depth=-1,
        theme=theme,
        invert_theme=True
    )

    return layout

