from dash import dcc, html


def get_radioitem_layout(
        title,
        title_id,
        list_of_options,
        default_value,
        verbose=False
    ):
    if verbose:
        print(f'Call get_radioitem_layout(): title={title}, title_id={title_id}, list_of_options={list_of_options}, default_value={default_value}')

    layout = html.Div(
        children=[
            html.H4(title),
            dcc.RadioItems(
                id=title_id,
                options=list_of_options,
                value=default_value,
                style={
                    'padding': 20,
                    'flex': 10,
                },
            ),
        ],
    )

    return layout


##################################################
#
# Layout for control panel
#
##################################################


def get_control_panel_contents_layout(verbose=False):
    if verbose:
        print(f'Call get_control_panel_contents_layout():')

    layout = html.Div(
        children=[
            html.Div(
                id='configs',
                children=get_radioitem_layout(
                    title='Config Files',
                    title_id='radioItems-configs',
                    list_of_options=[
                        'Config File Reader',
                    ],
                    default_value=None
                ),
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
            html.Br(),

            html.Div(
                id='metadata',
                children=get_radioitem_layout(
                    title='Meta Data',
                    title_id='radioItems-metadata',
                    list_of_options=[
                        'Network Analyzer Layer',
                        'Model Layer',
                    ],
                    default_value=None
                ),
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
            html.Br(),

            html.Div(
                id='simulation',
                children=get_radioitem_layout(
                    title='Simulation',
                    title_id='radioItems-simulation',
                    list_of_options=[
                        'AP&I',
                        'Traditional Supply Chain',
                        'Simulator',
                    ],
                    default_value=None
                ),
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
            html.Br(),

            html.Div(
                id='forecast',
                children=get_radioitem_layout(
                    title='Forecast',
                    title_id='radioItems-forecast',
                    list_of_options=[
                        'Order',
                        'Demand'
                    ],
                    default_value=None
                ),
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
            html.Br(),
        ],
        style={'display': 'flex'},
    )

    return layout

