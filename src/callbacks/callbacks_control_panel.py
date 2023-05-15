import json
from dash import html, dcc, callback, Input, Output, State
from src.callbacks.callbacks_common import logger
from src.layouts.layouts_control_panel import get_control_panel_contents_layout


##################################################
#
# callback functions for control_panel
#
##################################################


@callback(
    Output(component_id='store-cloud-setting', component_property='data'),
    Input(component_id='dropdown-cloud-service', component_property='value'),
    Input(component_id='dropdown-project', component_property='value'),
    Input(component_id='dropdown-bucket', component_property='value'),
    Input(component_id='dropdown-customer-name', component_property='value')
)
def update_cloud_setting(
        cloud_service,
        project,
        bucket,
        customer_name
    ):
    logger.info('Call callback: update_cloud_setting()')
    logger.info(f'\tSelect: cloud_service={cloud_service}, project={project}, bucket={bucket}, customer={customer_name}')

    if cloud_service == 'Azure':
        cloud_service = 'azure'
    elif cloud_service == 'Google Cloud Platform':
        cloud_service = 'gcp'
    elif cloud_service == 'Amazon AWS':
        cloud_service = 's3'

    cloud_setting = {
        'cloud_service': cloud_service,
        'project': project,
        'bucket': bucket,
        'customer_name': customer_name,
    }
    logger.info(f'\tSet cloud_setting={cloud_setting} as type={type(cloud_setting)}')

    return json.dumps(cloud_setting)


@callback(
    Output(component_id='hidden-div-control-panel', component_property='children'),
    # Output(component_id='configs', component_property='children'), 
    # Output(component_id='metadata', component_property='children'),
    # Output(component_id='simulation', component_property='children'),
    # Output(component_id='forecast', component_property='children'),
    Output(component_id='control-panel-contents', component_property='children'),
    Input(component_id='radioItems-configs', component_property='value'),
    Input(component_id='radioItems-metadata', component_property='value'),
    Input(component_id='radioItems-simulation', component_property='value'),
    Input(component_id='radioItems-forecast', component_property='value'),
)
def open_analyzer(config_value, metadata_value, simulation_value, forecast_value):
    logger.info('Call callback: open_analyzer()')

    redirect_destination= None
    # Configs
    if config_value == 'Config File Reader':
        logger.info(f'\tClick configs->{config_value}, open Config File Reader')
        redirect_destination = dcc.Location(
            id='pages-configs',
            pathname='/config-reader',
        )
    
    # Meta Data
    if metadata_value == 'Network Analyzer Layer':
        logger.info(f'\tClick metadata->{metadata_value}, open Network Analyzer layer')
        redirect_destination = dcc.Location(
            id='pages-metadata-network-analyzer-layer',
            pathname='/metadata-network-analyzer-layer',
        )
    elif metadata_value == 'Model Layer':
        logger.info(f'\tClick metadata->{metadata_value}, open Model layer')
        redirect_destination = dcc.Location(
            id='pages-metadata-network-analyzer-layer',
            pathname='/metadata-model-layer',
        )

    # Simulation
    if simulation_value == 'AP&I':
        logger.info(f'\tClick simulation->{simulation_value}, open AP&I analyzer')
        redirect_destination = dcc.Location(
            id='pages-simulation-apni',
            pathname='/simulation-apni',
        )
    elif simulation_value == 'Traditional Supply Chain':
        logger.info(f'\tClick simulation->{simulation_value}, open Traditional analyzer')
        redirect_destination = dcc.Location(
            id='pages-simulation-traditional',
            pathname='/simulation-traditional',
        )
    elif simulation_value == 'Simulator':
        logger.info(f'\tClick simulation->{simulation_value}, open Simulator analyzer')
        redirect_destination = dcc.Location(
            id='pages-simulation-simulator',
            pathname='/simulation-simulator',
        )

    # Forecast
    if forecast_value == 'Order':
        logger.info(f'\tClick forecast->{forecast_value}, open order forecast')
        redirect_destination = dcc.Location(
            id='pages-forecast-order',
            pathname='/forecast-order',
        )
    elif forecast_value == 'Demand':
        logger.info(f'\tClick forecast->{forecast_value}, open demand forecast')
        redirect_destination = dcc.Location(
            id='pages-forecast-demand',
            pathname='/forecast-demand',
        )

    # Reset radio items
    # Because metadata, simulation, and forecast sections are independent,
    # We have to avoid users select an item in each section. We only allow
    # one item to be selected

    # config_children=[
    #     html.H4('Config Files'),
    #     dcc.RadioItems(
    #         id='radioItems-configs',
    #         options=[
    #             'Config File Reader',
    #         ],
    #         value=None,
    #         style={
    #             'padding': 20,
    #             'flex': 10
    #         },  
    #     ),
    # ]

    # metadata_children=[
    #     html.H4('Meta Data'),
    #     # html.Label(children='Meta Data'),
    #     dcc.RadioItems(
    #         id='radioItems-metadata',
    #         options=[
    #             'Network Analyzer Layer',
    #             'Model Layer'
    #         ],
    #         value=None,
    #         style={
    #             'padding': 20,
    #             'flex': 10
    #         },  
    #     ),
    # ]

    # simulation_children=[
    #     html.H4('Simulation'),
    #     # html.Label('Simulation'),
    #     dcc.RadioItems(
    #         id='radioItems-simulation',
    #         options=[
    #             'AP&I',
    #             'Traditional Supply Chain',
    #             'Simulator'
    #         ],
    #         value=None,
    #         style={
    #             'padding': 20,
    #             'flex': 10
    #         }, 
    #     ),
    # ]
    
    # forecast_children=[
    #     html.H4('Forecast'),
    #     # html.Label(['Forecast']),
    #     dcc.RadioItems(
    #         id='radioItems-forecast',
    #         options=[
    #             'Order',
    #             'Demand'
    #         ],
    #         value=None,
    #         style={
    #             'padding': 20,
    #             'flex': 10
    #         }, 
    #     ),
    # ]

    # return redirect_destination, config_children, metadata_children, simulation_children, forecast_children
    return redirect_destination, get_control_panel_contents_layout()


