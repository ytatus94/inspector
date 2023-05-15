from datetime import date
from dash import dcc, html


##################################################
#
# Layout for common parts
#
##################################################


def get_title_section_layout(page_name):
    layout = html.Div(
        id='page-title-section',
        children=[
            html.Div(
                children=[
                    html.H1(
                        id='page-title-control-panel',
                        children=page_name,
                        className='page-title',
                        style={
                            'font-weight': 'bold',
                            'text-align': 'left'
                        },
                    ),
                ],
                #style={'width': '80%', 'border-style': 'dotted'},
                style={'width': '80%'},
            ),

            html.Div(
                children=[
                    html.H1(
                        id='seeloz',
                        children='SEELOZ',
                        className='seeloz-logo',
                        style={
                            'font-family': 'Sans-serif',
                            'font-weight': 'bold',
                            'color': 'Tomato',
                            'text-align': 'right'
                        },
                    )
                ],
                #style={'width': '20%', 'border-style': 'dotted'},
                style={'width': '20%'},
            ),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_cloud_setting_layout():
    layout = html.Div(
        id='cloud-setting-section',
        children=[
            # Cloud Service
            html.Div(
                children=[
                    html.Label('Select Cloud Service:'),
                    dcc.Dropdown( 
                        id='dropdown-cloud-service',
                        placeholder='Cloud',
                        options=[
                            {'label': 'Azure', 'value': 'Azure'},
                            {'label': 'Google Cloud Platform', 'value': 'GCP'},
                            {'label': 'Amazon AWS', 'value': 'S3'},
                        ],
                        value='Azure',
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Project
            html.Div(
                children=[
                    html.Label('Select Project:'),
                    dcc.Dropdown( 
                        id='dropdown-project',
                        placeholder='Project',
                        options=[
                            {'label': 'seelozdevelop', 'value': 'seelozdevelop'},
                        ],
                        value='seelozdevelop',
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Bucket
            html.Div(
                children=[
                    html.Label('Select Bucket:'),
                    dcc.Dropdown( 
                        id='dropdown-bucket',
                        placeholder='Bucket',
                        options=[
                            {'label': 'dev', 'value': 'dev'},
                            {'label': 'prod', 'value': 'prod'},
                            {'label': 'test', 'value': 'test'},
                        ],
                        value='dev',
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),

            # Customer Name
            html.Div(
                children=[
                    html.Label('Select Customer:'),
                    dcc.Dropdown( 
                        id='dropdown-customer-name',
                        placeholder='Customer Name',
                        options=[
                            {'label': 'Ides', 'value': 'ides'},
                            {'label': 'Unifi', 'value': 'unifi'},
                            {'label': 'Ingress', 'value': 'ingress'},
                            {'label': 'Pactiv', 'value': 'pactiv'},
                            {'label': 'Supply Side', 'value': 'supplyside'},
                            {'label': 'Aramco', 'value': 'aramco'},
                        ],
                        value='ingress',
                        searchable=False,
                        clearable=False,
                        multi=False,
                    ),
                ],
                style={
                    'width': '20%',
                    'margin': '10px 10px 10px 10px'
                },
            ),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_text_input_and_button_layout(
        title,
        input_text,
        input_id,
        button_text,
        button_id
    ):
    layout = html.Div(
        id='input-path-section',
        children=[
            # title
            html.Div(
                children=[
                    html.H6(title)
                ],
                style={'width': '10%', 'margin': '10px 10px 10px 10px'},
            ),
            # text field
            html.Div(
                children=[
                    dcc.Input(
                        id=input_id,
                        type='text',
                        value=input_text,
                        style={'width': '100%'},
                    ),
                    
                ],
                style={'width': '43%', 'margin': '10px 10px 10px 10px'},
            ),
            # button
            html.Div(
                children=[
                    html.Button(
                        id=button_id,
                        n_clicks=0,
                        children=button_text,
                        style={'width': '100%'},
                    ),
                ],
                style={'width': '20%', 'margin': '10px 10px 10px 10px'},
            ),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_historical_data_path_layout(default_path):
    layout = get_text_input_and_button_layout(
        title='Historical Data Path:',
        input_text=default_path,
        input_id='input-historical-data-path',
        button_text='Confirm',
        button_id='button-confirm-historical-path'
    )

    return layout


def get_input_data_path_layout(
        title,
        default_path,
        input_id,
        button_id
    ):
    layout = get_text_input_and_button_layout(
        title=title,
        input_text=default_path,
        input_id=input_id,
        button_text='Confirm',
        button_id=button_id
    )

    return layout


# def get_input_data_path_layout(default_path):
#     layout = html.Div(
#         id='input-path-section',
#         children=[
#             # text field
#             html.Div(
#                 children=[
#                     dcc.Input(
#                         id='input-data-path',
#                         type='text',
#                         value=default_path,
#                         style={'width': '100%'},
#                     ),
                    
#                 ],
#                 style={'width': '63%', 'margin': '10px 10px 10px 10px'},
#             ),
#             # button
#             html.Div(
#                 children=[
#                     html.Button(
#                         id='button-confirm',
#                         n_clicks=0,
#                         children='Confirm',
#                         style={'width': '100%'},
#                     ),
#                 ],
#                 style={'width': '20%', 'margin': '10px 10px 10px 10px'},
#             ),
#         ],
#         style={'display': 'flex'},
#     )

#     return layout


def get_dropdown_filter_layout(
        dropdown_label,
        dropdown_id,
        all_options,
        default_option,
        searchable=False,
        clearable=False,
        multi=False
    ):
    layout = html.Div(
        children=[
            html.Label([dropdown_label]),
            dcc.Dropdown( 
                id=dropdown_id,
                options=all_options,
                value=default_option,
                searchable=searchable,
                clearable=clearable,
                multi=multi,
            ),
        ],
        style={'width': '20%', 'margin': '10px 10px 10px 10px'},
    )

    return layout


def get_wid_pid_filter_layout(all_options):
    layout = get_dropdown_filter_layout(
        dropdown_label='(Warehousd ID, Product ID):',
        dropdown_id='dropdown-pair',
        all_options=all_options,
        default_option=all_options[0]['value'],
    )

    return layout


# def get_wid_pid_filter_layout(all_options):
#     layout = html.Div(
#         children=[
#             html.Label(['(Warehousd ID, Product ID):']),
#             dcc.Dropdown( 
#                 id='dropdown-pair',
#                 options=all_options,
#                 value=all_options[0]['value'],
#                 searchable=False,
#                 clearable=False,
#                 multi=False,
#             ),
#         ],
#         style={'width': '20%', 'margin': '10px 10px 10px 10px'},
#     )

#     return layout


def get_date_range_filter_layout(start_date, end_date):
    layout = html.Div(
        children=[
            html.Label(['Date range:']), 
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=start_date, 
                end_date=end_date, 
                display_format='YYYY-MM-Do'
            ),
        ],
        style={'width': '50%', 'margin': '10px 10px 10px 10px'},
    )

    return layout


def get_hidden_layout():
    # This is a dummy object used for callback no output
    layout = html.Div(
        id='div-hidden-layout',
        style={'display': 'none'}
    )

    return layout


