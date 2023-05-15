import dash_renderjson
import json
import pandas as pd
from dash import html, dcc, callback, Input, Output, State
# from dash import html, dcc, callback, State
# from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform
# from dash_extensions.enrich import Output, Input
from src.layouts.layouts_common import get_wid_pid_filter_layout, get_historical_data_path_layout, get_input_data_path_layout
from src.layouts.layouts_apni import get_apni_results_contents, get_apni_comparison_contents, get_apni_results_layout, get_apni_results_filter
from src.callbacks.callbacks_common import logger, dict_dh_objects
from src.utils.cloud_setting import get_DataHandler_object
from src.utils.load_data import load_data


def update_historical_and_apni_data(
        cloud_setting,
        historical_data_path,
        apni_results_path,
        force_reload
    ):
    logger.info(f'Call update_historical_and_apni_data(): historical_data_path={historical_data_path}, apni_results_path={apni_results_path}, force_reload={force_reload}')

    dh_object = get_DataHandler_object(
        dict_dh_objects=dict_dh_objects,
        cloud_service=cloud_setting['cloud_service'],
        project=cloud_setting['project'],
        bucket=cloud_setting['bucket'],
        customer_name=cloud_setting['customer_name'],
    )

    path = '/'.join(historical_data_path.split('/')[:-2]) + '/'
    table_name = historical_data_path.split('/')[-2] # should be 'inventory_levels'
    # print(f'path={path}, table_name={table_name}')

    df_inventory = load_data(
        dh_object=dh_object,
        path=path,
        table_name=table_name,
        force_reload=force_reload
    )
    print(f'df_inventory:\n{df_inventory.head()}')
    print(df_inventory.info())

    df_ai = load_data(
        dh_object=dh_object,
        path=apni_results_path,
        table_name='AI',
        force_reload=force_reload
    )
    print(f'df_ai:\n{df_ai.head()}')
    print(df_ai.info())

    df_tr = load_data(
        dh_object=dh_object,
        path=apni_results_path,
        table_name='TR',
        force_reload=force_reload
    )
    print(f'df_tr:\n{df_tr.head()}')
    print(df_tr.info())


##################################################
#
# callback functions for simulation AP&I
#
##################################################


@callback(
    Output(component_id='singlewarehouse-data-path', component_property='children'),
    Input(component_id='store-cloud-setting', component_property='data'),
)
def update_input_data_path(cloud_setting):
    logger.info(f'Call update_input_data_path():')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')

    customer_name = cloud_setting['customer_name']
    historical_data_path = f'customers/{customer_name}/model/inventory_levels/'
    logger.info(f'\tCurrent historical_data_path={historical_data_path}')
    apni_results_path = f'customers/{customer_name}/apni/singlewarehouse/results/latest/'
    logger.info(f'\tCurrent apni_results_path={apni_results_path}')

    layout = html.Div(
        children=[
            get_historical_data_path_layout(historical_data_path),
            get_input_data_path_layout(
                title='AP&I Results Path:',
                default_path=apni_results_path,
                input_id='input-data-path',
                button_id='button-confirm'
            ),
        ],
    )

    # Because the data paths are changed when the page is launched, 
    # we have to update data too
    # update_historical_and_apni_data(
    #     cloud_setting=cloud_setting,
    #     historical_data_path=historical_data_path,
    #     apni_results_path=apni_results_path,
    #     force_reload=True
    # )

    return layout


@callback(
    Output(component_id='hidden-div-simulation-apni', component_property='children'),
    Input(component_id='button-confirm-historical-path', component_property='n_clicks'),
    Input(component_id='button-confirm', component_property='n_clicks'),
    State(component_id='input-historical-data-path', component_property='value'),
    State(component_id='input-data-path', component_property='value'),
    State(component_id='store-cloud-setting', component_property='data'),
)
def update_input_data(
        click_historical_path_button,
        click_apni_path_button,
        historical_data_path,
        apni_results_path,
        cloud_setting
    ):
    logger.info(f'Call update_input_data(): historical_data_path={historical_data_path}, apni_results_path={apni_results_path}')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')
    
    # Because the user changes the historical and ap&i input data path,
    # we force to reload the data from remote.
    update_historical_and_apni_data(
        cloud_setting=cloud_setting,
        historical_data_path=historical_data_path,
        apni_results_path=apni_results_path,
        force_reload=True
    )

    # dummy layout
    layout = html.Div()

    return layout


@callback(
    Output(component_id='simulation-apni-contents', component_property='children'),
    Input(component_id='tabs-simulation-apni', component_property='value'),
)
def click_tab(tab_value):
    logger.info(f'Call click_tabs(): tab_value={tab_value}')

    if tab_value == 'tab_singlewarehouse_results':
        return get_apni_results_contents()
    elif tab_value == 'tab_singlewarehouse_comparisons':
        return get_apni_comparison_contents()


# @callback(
#     Output(component_id='simulation-apni-filters', component_property='children'),
#     Input(component_id='button-confirm-historical-path', component_property='n_clicks'),
#     Input(component_id='button-confirm', component_property='n_clicks'),
#     State(component_id='input-historical-data-path', component_property='value'),
#     State(component_id='input-data-path', component_property='value'),
# )
# def update_filters(
#         click_historical_path_button,
#         click_apni_path_button,
#         historical_data_path,
#         apni_results_path,
#     ):
#     logger.info(f'Call update_filters(): historical_data_path={historical_data_path}, apni_results_path={apni_results_path}')

#     df_ai = None
#     # At this stage, the data should exist on the local
#     try:
#         df_ai = pd.read_parquet('temp/apni/df_AI.parquet')
#         # print(f'df_ai:\n{df_ai.head()}')
#         # print(df_ai.info())
#     except FileNotFoundError:
#         logger.error('ERROR!!! The temp/apni/df_AI.parquet cannot be found on local.')

#     start_date = df_ai['date'].min()
#     end_date = df_ai['date'].max()
#     print(f'start_date={start_date}, type={type(start_date)}')
#     print(f'end_date={end_date}, type={type(end_date)}')

#     layout = get_apni_results_filter(
#         df=df_ai, 
#         start_date=start_date,
#         end_date=end_date
#     )

#     return layout


# @callback(
#     # Output(component_id='simulation-apni-filters', component_property='children'),
#     Output(component_id='simulation-apni-figure', component_property='figure'),
#     Output(component_id='simulation-apni-statistics', component_property='children'),
#     Input(component_id='tabs-simulation-apni', component_property='value'),
#     # State(component_id='input-historical-data-path', component_property='value'),
#     # State(component_id='input-data-path', component_property='value'),
#     Input(component_id='dropdown-pair', component_property='value'),
#     Input(component_id='date-picker-range', component_property='start_date'),
#     Input(component_id='date-picker-range', component_property='end_date'),
#     State(component_id='store-cloud-setting', component_property='data'),
# )
# def update_figure_and_statistics(
#         tab_value,
#         current_option,
#         start_date,
#         end_date,
#         cloud_setting
#     ):
#     logger.info(f'Call update_figure_and_statistics(): tab_value={tab_value}, current_option={current_option}, start_date={start_date}, end_date={end_date}, cloud_setting={cloud_setting}')
#     # logger.info(f'Call update_figure_and_statistics(): tab_value={tab_value}, cloud_setting={cloud_setting}')

#     cloud_setting = json.loads(cloud_setting)
#     logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')
    
#     # dh_object = get_DataHandler_object(
#     #     dict_dh_objects=dict_dh_objects,
#     #     cloud_service=cloud_setting['cloud_service'],
#     #     project=cloud_setting['project'],
#     #     bucket=cloud_setting['bucket'],
#     #     customer_name=cloud_setting['customer_name'],
#     # )

#     # Load data from local
#     df_inventory = None
#     df_ai = None
#     df_tr = None

#     # At this stage, the data should exist on the local
#     try:
#         df_inventory = pd.read_parquet('temp/model/df_inventory_levels.parquet')
#         # print(f'df_inventory:\n{df_inventory.head()}')
#         # print(df_inventory.info())
#     except FileNotFoundError:
#         logger.error('ERROR!!! The temp/model/df_inventory_levels.parquet cannot be found on local.')

#     try:
#         df_ai = pd.read_parquet('temp/apni/df_AI.parquet')
#         # print(f'df_ai:\n{df_ai.head()}')
#         # print(df_ai.info())
#     except FileNotFoundError:
#         logger.error('ERROR!!! The temp/apni/df_AI.parquet cannot be found on local.')

#     try:
#         df_tr = pd.read_parquet('temp/apni/df_TR.parquet')
#         # print(f'df_tr:\n{df_tr.head()}')
#         # print(df_tr.info())
#     except FileNotFoundError:
#         logger.error('ERROR!!! The temp/apni/df_TR.parquet cannot be found on local.')

#     if tab_value == 'tab_singlewarehouse_results':
#         # start_date = df_ai['date'].min()
#         # end_date = df_ai['date'].max()
#         print(f'start_date={start_date}, type={type(start_date)}, df_ai["date"].min()={df_ai["date"].min()} , type(df_ai["date"].min())={type(df_ai["date"].min())}')
#         print(f'end_date={end_date}, type={type(end_date)}, df_ai["date"].min()={df_ai["date"].max()} , type(df_ai["date"].max())={type(df_ai["date"].max())}')


#         filters, figure, statistics = get_apni_results_layout(
#             df_historical=df_inventory,
#             df_ai=df_ai,
#             df_tr=df_tr,
#             current_option=current_option,
#             start_date=start_date,
#             end_date=end_date
#         )

#         return figure, statistics
#     elif tab_value == 'tab_singlewarehouse_comparisons':
#         return get_apni_comparisons_layout(
#             df_historical=df_inventory
#         )


# @callback(
#     # Output(component_id='simulation-apni-filters', component_property='children'),
#     Output(component_id='simulation-apni-figure', component_property='figure'),
#     Output(component_id='simulation-apni-statistics', component_property='children'),
#     Input(component_id='dropdown-pair', component_property='value'),
#     Input(component_id='date-picker-range', component_property='start_date'),
#     Input(component_id='date-picker-range', component_property='end_date'),
# )
# def update_apni_layouts(
#         wid_pid_pair,
#         start_date,
#         end_date
#     ):
#     logger.info(f'Call update_apni_layouts(): wid_pid_pair={wid_pid_pair}, start_date={start_date}, end_date={end_date}')

#     # At this stage, the data should exist on the local
#     try:
#         df_inventory = pd.read_parquet('temp/model/df_inventory_levels.parquet')
#         df_ai = pd.read_parquet('temp/apni/df_AI.parquet')
#         df_tr = pd.read_parquet('temp/apni/df_TR.parquet')
#     except FileNotFoundError:
#         logger.error('ERROR!!! The temp/model/df_inventory_levels.parquet or temp/apni/df_AI.parquet or temp/apni/df_TR.parquet cannot be found on local.')

#     figure = get_apni_results_figure(
#         df_historical=df_inventory,
#         df_ai=df_ai,
#         df_tr=df_tr,
#         current_option=wid_pid_pair,
#         start_date=start_date,
#         end_date=end_date
#     )

#     statistics = get_apni_results_statistics(
#         df_historical=df_inventory,
#         df_ai=df_ai,
#         df_tr=df_tr,
#         current_option=wid_pid_pair,
#         start_date=start_date,
#         end_date=end_date
#     )
    
#     return figure, statistics

