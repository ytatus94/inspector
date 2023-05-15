from dash import dcc, html, dash_table
import plotly.graph_objects as go
from src.layouts.layouts_common import get_wid_pid_filter_layout, get_date_range_filter_layout, get_input_data_path_layout
from src.utils.plot import plot_timeseries
from src.utils.sub_dataframe import get_sub_dataframe


def get_df_historical_group(
        df_historical,
        all_pids,
        start_date,
        end_date,
        cols,
        verbose=False
    ):
    print(f'Call get_df_historical_group(): all_pids={all_pids}, start_date={start_date}, end_date={end_date}, cols={cols}')

    df_historical_group = (
        get_sub_dataframe(
            df=df_historical,
            pids=all_pids,
            start_date=start_date,
            end_date=end_date,
            cols=['date', 'quantity']
        )
        .groupby('date')
        .sum()
        .reset_index()
        .rename(columns={'quantity': 'inventory'})
    )

    return df_historical_group


def get_df_sw_group(
        df_sw,
        start_date,
        end_date,
        cols,
        verbose=False
    ):
    '''
    df_sw can be df_ai or df_tr
    '''
    print(f'Call get_df_sw_group(): start_date={start_date}, end_date={end_date}')

    df_sw_group = (
        get_sub_dataframe(
            df=df_sw,
            start_date=start_date,
            end_date=end_date,
            cols=['date', 'inventory']
        )
        .groupby('date')
        .sum()
        .reset_index()
    )

    return df_sw_group


##################################################
#
# Layout for simulation AP&I
#
##################################################


def get_apni_results_contents():
    print(f'Call get_apni_results_contents():')

    layout = html.Div(
        children=[
            html.Div(
                id='simulation-apni-filters',
                children=[
                    get_wid_pid_filter_layout([
                        {'label': 'all', 'value': 'all'},
                    ]),
                    get_date_range_filter_layout(
                        start_date='2021-01-01',
                        end_date='2021-12-31'
                    )
                ],
                style={'display': 'flex'},
            ),

            html.Div(
                children=[
                    html.H4('Time Series Distribution:'),
                    dcc.Graph(id='simulation-apni-figure'),
                ],
            ),
            html.Br(),

            html.Div(
                children=[
                    html.H4('Statistics:'),
                    html.Div(id='simulation-apni-statistics'),
                ],
            ),
            html.Br(),

            html.Div(
                children=[
                    html.H4('Table:'),
                    html.Div(id='simulation-apni-table'),
                ],
            ),
            html.Br(),
        ],
    )

    return layout


def get_apni_comparison_contents():
    print(f'Call get_apni_comparison_contents()')

    default_path = None

    layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.H1('Under construction...'),
                    html.H4('Different AP&I results path: (Support upto 5 different AP&I results)'),
                    get_input_data_path_layout('AP&I Results 2 Path:', default_path, 'input_id_2', 'button_id_2'),
                    get_input_data_path_layout('AP&I Results 3 Path:', default_path, 'input_id_3', 'button_id_3'),
                    get_input_data_path_layout('AP&I Results 4 Path:', default_path, 'input_id_4', 'button_id_4'),
                    get_input_data_path_layout('AP&I Results 5 Path:', default_path, 'input_id_5', 'button_id_5'),
                ],
            ),
            html.Br(),

            html.Div(
                children=[
                    html.H4('Time Series Distribution:'),
                    dcc.Graph(id='simulation-apni-figure'),
                ],
            ),
            html.Br(),

            html.Div(
                children=[
                    html.H4('Statistics:'),
                    html.Div(id='simulation-apni-statistics'),
                ],
            ),
            html.Br(),

            html.Div(
                children=[
                    html.H4('Table:'),
                    html.Div(id='simulation-apni-table'),
                ],
            ),
            html.Br(),
        ],
    )

    return layout


def get_apni_results_filter(
        df,
        start_date,
        end_date,
        verbose=False
    ):
    print(f'Call get_apni_results_filter(): start_date={start_date}, end_date={end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    # print(len(pairs), pairs)
    print(f'Number of pairs={len(pairs)}')

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    # print(len(all_options), all_options)
    # print(len(all_options))

    layout = html.Div(
        id='filter-section',
        children=[
            get_wid_pid_filter_layout(all_options),
            get_date_range_filter_layout(start_date, end_date),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_apni_results_figure(
        df_historical,
        df_ai,
        df_tr,
        current_option,
        start_date,
        end_date,
        verbose=False
    ):
    print(f'Call get_apni_results_figure(): current_option={current_option}, start_date={start_date}, end_date={end_date}')

    all_pids = df_ai['product_id'].unique().tolist()

    # figure = None
    title = None

    df_historical_plot = None
    df_ai_plot = None
    df_tr_plot = None

    if current_option == 'all':
        df_historical_plot = get_df_historical_group(
            df_historical=df_historical,
            all_pids=all_pids,
            start_date=start_date,
            end_date=end_date,
            cols=['date', 'quantity']
        )
        print(f'df_historical_group:\n{df_historical_plot.head()}')
        print(df_historical_plot.info())

        df_ai_plot = get_df_sw_group(
            df_sw=df_ai,
            start_date=start_date,
            end_date=end_date,
            cols=['date', 'inventory']
        )
        print(f'df_ai_group:\n{df_ai_plot.head()}')
        print(df_ai_plot.info())

        df_tr_plot = get_df_sw_group(
            df_sw=df_tr,
            start_date=start_date,
            end_date=end_date,
            cols=['date', 'inventory']
        )
        print(f'df_tr_group:\n{df_tr_plot.head()}')
        print(df_tr_plot.info())


        title = f'Inventory levels for all products between {start_date} and {end_date}'

    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0])
        pid = int(current_option.split(',')[1])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_historical_plot = (
            get_sub_dataframe(
                df=df_historical,
                wid=wid,
                pid=pid,
                start_date=start_date,
                end_date=end_date,
                cols=['date', 'quantity']
            )
            # .loc[:, ['date', 'quantity']]
            .rename(columns={'quantity': 'inventory'})
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_historical_sub:\n{df_historical_plot.head()}')
        print(df_historical_plot.info())

        df_ai_plot = (
            get_sub_dataframe(
                df=df_ai,
                wid=wid,
                pid=pid,
                start_date=start_date,
                end_date=end_date,
                cols=['date', 'inventory']
            )
        )
        print(f'df_ai_sub:\n{df_ai_plot.head()}')
        print(df_ai_plot.info())

        df_tr_plot = (
            get_sub_dataframe(
                df=df_tr,
                wid=wid,
                pid=pid,
                start_date=start_date,
                end_date=end_date,
                cols=['date', 'inventory']
            )
        )
        print(f'df_tr_sub:\n{df_tr_plot.head()}')
        print(df_tr_plot.info())

        title = f'Inventory levels for ({wid}, {pid}) between {start_date} and {end_date}'

    figure = plot_timeseries(
        df_historical_plot,
        x='date',
        y='inventory',
        title=title
    )

    figure.add_trace(
        go.Scatter(
            x=df_ai_plot['date'],
            y=df_ai_plot['inventory'],
            name='AI'
        )
    )

    figure.add_trace(
        go.Scatter(
            x=df_tr_plot['date'],
            y=df_tr_plot['inventory'],
            name='TR'
        )
    )

    # fig.update_layout(
    #     title="ICICI BANK stock prices", xaxis_title="Date", yaxis_title="Close"
    # )

    return figure

def get_apni_results_statistics(
        df_historical,
        df_ai,
        df_tr,
        current_option,
        start_date,
        end_date
    ):
    print(f'Call get_apni_results_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(
    )

    return layout


def get_apni_results_table(
        # df_historical,
        df_ai,
        df_tr,
        current_option,
        start_date,
        end_date
    ):
    print(f'Call get_apni_results_table(): {current_option}, {start_date}, {end_date}')

    df_ai_table = None
    df_tr_table = None

    if current_option == 'all':
        df_ai_table = get_sub_dataframe(
            df=df_ai,
            start_date=start_date,
            end_date=end_date
        )

        df_tr_table = get_sub_dataframe(
            df=df_tr,
            start_date=start_date,
            end_date=end_date
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_ai_table = get_sub_dataframe(
            df=df_ai,
            wid=wid,
            pid=pid,
            start_date=start_date,
            end_date=end_date
        )

        df_tr_table = get_sub_dataframe(
            df=df_tr,
            wid=wid,
            pid=pid,
            start_date=start_date,
            end_date=end_date
        )

    ai_table_layout = dash_table.DataTable(
        data=df_ai_table.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_ai_table.columns],
        page_size=15
    )

    tr_table_layout = dash_table.DataTable(
        data=df_tr_table.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_tr_table.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-inventory-levels',
        children=[
            html.H4('AI results:'),
            ai_table_layout,
            html.Br(),

            html.H4('TR results:'),
            tr_table_layout,
            html.Br(),
        ],
    )

    return layout


def get_apni_results_layout(
        df_historical,
        df_ai,
        df_tr,
        current_option,
        start_date,
        end_date
    ):
    print(f'Call get_apni_results_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_apni_results_filter(
        df=df_ai,
        start_date=start_date,
        end_date=end_date
    )
    figure = get_apni_results_figure(
        df_historical=df_historical,
        df_ai=df_ai,
        df_tr=df_tr,
        current_option=current_option,
        start_date=start_date,
        end_date=end_date
    )
    statistics = get_apni_results_statistics(
        df_historical=df_historical,
        df_ai=df_ai,
        df_tr=df_tr,
        current_option=current_option,
        start_date=start_date,
        end_date=end_date
    )
    # table = get_apni_results_table(
    #     df=df_ai,
    #     urrent_option=current_option,
    #     start_date=start_date,
    #     end_date=end_date
    # )

    return filters, figure, statistics


def get_apni_comparisons_layout(
        df_historical
    ):
    print(f'Call get_apni_comparisons_layout():')

    figure = None

    return figure

