# from datetime import date
from dash import dcc, html, dash_table
# import plotly.express as px
# import plotly.graph_objects as go
from src.layouts.layouts_common import get_wid_pid_filter_layout, get_date_range_filter_layout, get_dropdown_filter_layout
from src.utils.plot import plot_timeseries, plot_bar_chart


def get_options(df, column):
    column_ids = df[column].unique().tolist()
    # print(f'{column}: {len(column_ids)}, {column_ids}')
    print(f'{column}: {len(column_ids)}')

    column_id_options = [{'label': 'all', 'value': 'all'}]
    for col_id in column_ids:
        column_id_options.append({'label': f'{col_id}', 'value': f'{col_id}'})
    # print(len(column_id_options), column_id_options)
    # print(len(column_id_options))

    return column_id_options


# def plot_timeseries(df, x, y, title):
#     figure = px.line(
#         df,
#         x=x,
#         y=y,
#         title=title,
#     )
#     figure.update_layout(hovermode='x unified')
#     print('figure should be ready')

#     return figure


# def plot_bar_chart(df, x, y, title):
#     figure = px.bar(
#         df,
#         x=x,
#         y=y,
#         title=title,
#     )
#     figure.update_layout(hovermode='x unified')
#     print('figure should be ready')

#     return figure


##################################################
#
# inventory levels table
#
##################################################


def get_inventory_filter(df, start_date, end_date):
    print(f'Call get_inventory_filter(): {start_date} {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    # print(len(pairs), pairs)
    print(len(pairs))

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


def get_inventory_figure(df, current_option, start_date, end_date):
    print(f'Call get_inventory_plot(): {current_option}, {start_date}, {end_date}')

    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
            .rename(columns={'quantity': 'inventory'})
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_timeseries(
            df_group,
            x='date',
            y='inventory',
            title=f'Inventory levels for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .rename(columns={'quantity': 'inventory'})
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_timeseries(
            df_sub,
            x='date',
            y='inventory',
            title=f'Inventory levels for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_inventory_statistics(df, current_option, start_date, end_date):
    print(f'Call get_inventory_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(
    )

    return layout


def get_inventory_table(df, current_option, start_date, end_date):
    print(f'Call get_inventory_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-inventory-levels',
        children=[table_layout],
    )

    return layout


def get_inventory_layout(df, current_option, start_date, end_date):
    print(f'Call get_inventory_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_inventory_filter(df, start_date, end_date)
    figure = get_inventory_figure(df, current_option, start_date, end_date)
    statistics = get_inventory_statistics(df, current_option, start_date, end_date)
    # By showing table, it slows down the dashboard a lot.
    # table = get_inventory_table(df, current_option, start_date, end_date)

    return filters, figure, statistics

##################################################
#
# demand table
#
##################################################


def get_demand_filter(df, start_date, end_date):
    print(f'Call get_demand_filter(): {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_demand_figure(df, current_option, start_date, end_date):
    print(f'Call get_demand_figure(): {current_option}, {start_date}, {end_date}')
 
    layout = html.Div(
        html.H4('Not support yet')
    )

    return layout


def get_demand_statistics(df, current_option, start_date, end_date):
    print(f'Call get_demand_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_demand_table(df, current_option, start_date, end_date):
    print(f'Call get_demand_table(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_demand_layout(dict_dfs, current_option, start_date, end_date):
    print(f'Call get_demand_layout(): {current_option}, {start_date}, {end_date}')

    df_mdo = dict_dfs['monthly_demand_from_orders']
    df_mdd = dict_dfs['monthly_demand_from_deliveries']
    df_ddo = dict_dfs['daily_demand_from_orders']
    df_ddd = dict_dfs['daily_demand_from_deliveries']

    filters = get_demand_filter(df, start_date, end_date)
    figure = get_demand_figure(df, current_option, start_date, end_date)
    statistics = get_demand_statistics(df, current_option, start_date, end_date)
    table = get_demand_table(df, current_option, start_date, end_date)

    return filters, figure, statistics, table


##################################################
#
# orders table
#
##################################################


def get_orders_filter(df, start_date, end_date):
    print(f'Call get_orders_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    # print(len(all_options))

    # order_id_options = get_options(df, 'order_id')
    customer_id_options = get_options(df, 'customer_id')
    site_id_options = get_options(df, 'site_id')

    layout = html.Div(
        id='filter-section',
        children=[
            get_wid_pid_filter_layout(all_options),
            # Because there are too many order_ids, it slows down the dashboard a lot. 
            # get_dropdown_filter_layout(
            #     dropdown_label='Order ID',
            #     dropdown_id='dropdown-order-id',
            #     all_options=order_id_options,
            #     default_option='all'
            # ),
            get_dropdown_filter_layout(
                dropdown_label='Customer ID:',
                dropdown_id='dropdown-customer-id',
                all_options=customer_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Site ID:',
                dropdown_id='dropdown-site-id',
                all_options=site_id_options,
                default_option='all'
            ),
            get_date_range_filter_layout(start_date, end_date),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_orders_figure(df, current_option, start_date, end_date):
    print(f'Call get_orders_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'ordered_quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='ordered_quantity',
            title=f'Orders for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'ordered_quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='inventory',
            title=f'Orders for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_orders_statistics(df, current_option, start_date, end_date):
    print(f'Call get_orders_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_orders_table(df, current_option, start_date, end_date):
    print(f'Call get_orders_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-orders',
        children=[table_layout],
    )

    return layout


def get_orders_layout(df, current_option, start_date, end_date):
    print(f'Call get_orders_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_orders_filter(df, start_date, end_date)
    figure = get_orders_figure(df, current_option, start_date, end_date)
    statistics = get_orders_statistics(df, current_option, start_date, end_date)
    # table = get_orders_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# deliveries table
#
##################################################


def get_deliveries_filter(df, start_date, end_date):
    print(f'Call get_deliveries_filter(): {start_date}, {end_date}')

    warehouse_id_options = get_options(df, 'warehouse_id')
    # order_id_options = get_options(df, 'order_id')
    # delivery_header_id_options = get_options(df, 'delivery_header_id')
    delivery_item_id_options = get_options(df, 'delivery_item_id')
    site_id_options = get_options(df, 'site_id')
    customer_id_options = get_options(df, 'customer_id')
    # delivery_id_options = get_options(df, 'delivery_id')

    layout = html.Div(
        id='filter-section',
        children=[
            get_dropdown_filter_layout(
                dropdown_label='Warehouse ID:',
                dropdown_id='dropdown-warehouse-id',
                all_options=warehouse_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Customer ID:',
                dropdown_id='dropdown-customer-id',
                all_options=customer_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Site ID:',
                dropdown_id='dropdown-site-id',
                all_options=site_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Delivery Item ID:',
                dropdown_id='dropdown-delivery-item-id',
                all_options=delivery_item_id_options,
                default_option='all'
            ),
            get_date_range_filter_layout(start_date, end_date),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_deliveries_figure(df, current_option, start_date, end_date):
    print(f'Call get_deliveries_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='quantity',
            title=f'Deliveries for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='quantity',
            title=f'Deliveries for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_deliveries_statistics(df, current_option, start_date, end_date):
    print(f'Call get_deliveries_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_deliveries_table(df, current_option, start_date, end_date):
    print(f'Call get_deliveries_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-deliveries',
        children=[table_layout],
    )

    return layout


def get_deliveries_layout(df, current_option, start_date, end_date):
    print(f'Call get_deliveries_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_deliveries_filter(df, start_date, end_date)
    figure = get_deliveries_figure(df, current_option, start_date, end_date)
    statistics = get_deliveries_statistics(df, current_option, start_date, end_date)
    # table = get_deliveries_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# purchases table
#
##################################################


def get_purchases_filter(df, start_date, end_date):
    print(f'Call get_purchases_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    # print(len(all_options))

    # purchase_id_options = get_options(df, 'purchase_id')
    # purchase_header_id_options = get_options(df, 'purchase_header_id')
    purchase_line_id_options = get_options(df, 'purchase_line_id')
    supplier_id_options = get_options(df, 'supplier_id')
    supply_depot_id_options = get_options(df, 'supply_depot_id')

    layout = html.Div(
        id='filter-section',
        children=[
            get_wid_pid_filter_layout(all_options),
            # get_dropdown_filter_layout(
            #     dropdown_label='Purchase ID:',
            #     dropdown_id='dropdown-purchase-id',
            #     all_options=purchase_id_options,
            #     default_option='all'
            # ),
            # get_dropdown_filter_layout(
            #     dropdown_label='Purchase Header ID:',
            #     dropdown_id='dropdown-purchase-header-id',
            #     all_options=purchase_header_id_options,
            #     default_option='all'
            # ),
            get_dropdown_filter_layout(
                dropdown_label='Purchase Line ID:',
                dropdown_id='dropdown-purchase-line-id',
                all_options=purchase_line_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Supplier ID:',
                dropdown_id='dropdown-supplier-id',
                all_options=supplier_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Supply Depot ID:',
                dropdown_id='dropdown-supply-depot-id',
                all_options=supply_depot_id_options,
                default_option='all'
            ),
            get_date_range_filter_layout(start_date, end_date),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_purchases_figure(df, current_option, start_date, end_date):
    print(f'Call get_purchases_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='quantity',
            title=f'Purchases for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='quantity',
            title=f'Purchases for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_purchases_statistics(df, current_option, start_date, end_date):
    print(f'Call get_purchases_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_purchases_table(df, current_option, start_date, end_date):
    print(f'Call get_purchases_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-purchases',
        children=[table_layout],
    )

    return layout


def get_purchases_layout(df, current_option, start_date, end_date):
    print(f'Call get_purchases_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_purchases_filter(df, start_date, end_date)
    figure = get_purchases_figure(df, current_option, start_date, end_date)
    statistics = get_purchases_statistics(df, current_option, start_date, end_date)
    # table = get_purchases_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# procurements table
#
##################################################


def get_procurements_filter(df, start_date, end_date):
    print(f'Call get_procurements_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
    # print(len(all_options))

    supply_depot_id_options = get_options(df, 'supply_depot_id')
    # purchase_id_options = get_options(df, 'purchase_id')
    # procurement_id_options = get_options(df, 'procurement_id')
    supplier_id_options = get_options(df, 'supplier_id')


    layout = html.Div(
        id='filter-section',
        children=[
            get_wid_pid_filter_layout(all_options),
            get_dropdown_filter_layout(
                dropdown_label='Supplier ID:',
                dropdown_id='dropdown-supplier-id',
                all_options=supplier_id_options,
                default_option='all'
            ),
            get_dropdown_filter_layout(
                dropdown_label='Supply Depot ID:',
                dropdown_id='dropdown-supply-depot-id',
                all_options=supply_depot_id_options,
                default_option='all'
            ),
            get_date_range_filter_layout(start_date, end_date),
        ],
        style={'display': 'flex'},
    )

    return layout


def get_procurements_figure(df, current_option, start_date, end_date):
    print(f'Call get_procurements_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='quantity',
            title=f'Procurements for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='quantity',
            title=f'Procurements for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_procurements_statistics(df, current_option, start_date, end_date):
    print(f'Call get_procurements_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_procurements_table(df, current_option, start_date, end_date):
    print(f'Call get_procurements_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-procurements',
        children=[table_layout],
    )

    return layout


def get_procurements_layout(df, current_option, start_date, end_date):
    print(f'Call get_procurements_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_procurements_filter(df, start_date, end_date)
    figure = get_procurements_figure(df, current_option, start_date, end_date)
    statistics = get_procurements_statistics(df, current_option, start_date, end_date)
    # table = get_procurements_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# lead_time table
#
##################################################


def get_lead_time_filter(df, start_date, end_date):
    print(f'Call get_lead_time_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
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


def get_lead_time_figure(df, current_option, start_date, end_date):
    print(f'Call get_lead_time_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['order_date']>=start_date)&
                (df['order_date']<=end_date),
                ['order_date', 'lead_time']
            ]
            .groupby('order_date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='order_date',
            y='lead_time',
            title=f'Lead time for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['order_date']>=start_date)&
                (df['order_date']<=end_date),
                ['order_date', 'lead_time']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='order_date',
            y='lead_time',
            title=f'Lead time for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_lead_time_statistics(df, current_option, start_date, end_date):
    print(f'Call get_lead_time_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_lead_time_table(df, current_option, start_date, end_date):
    print(f'Call get_lead_time_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-lead-time',
        children=[table_layout],
    )

    return layout


def get_lead_time_layout(df, current_option, start_date, end_date):
    print(f'Call get_lead_time_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_lead_time_filter(df, start_date, end_date)
    figure = get_lead_time_figure(df, current_option, start_date, end_date)
    statistics = get_lead_time_statistics(df, current_option, start_date, end_date)
    # table = get_lead_time_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# stock_outs table
#
##################################################


def get_stock_outs_filter(df, start_date, end_date):
    print(f'Call get_stock_outs_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
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


def get_stock_outs_figure(df, current_option, start_date, end_date):
    print(f'Call get_stock_outs_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='quantity',
            title=f'Stock outs for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='quantity',
            title=f'Stock outs for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_stock_outs_statistics(df, current_option, start_date, end_date):
    print(f'Call get_stock_outs_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_stock_outs_table(df, current_option, start_date, end_date):
    print(f'Call get_stock_outs_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-stock-outs',
        children=[table_layout],
    )

    return layout


def get_stock_outs_layout(df, current_option, start_date, end_date):
    print(f'Call get_stock_outs_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_stock_outs_filter(df, start_date, end_date)
    figure = get_stock_outs_figure(df, current_option, start_date, end_date)
    statistics = get_stock_outs_statistics(df, current_option, start_date, end_date)
    # table = get_stock_outs_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


##################################################
#
# safety_stock table
#
##################################################


def get_safety_stock_filter(df, start_date, end_date):
    print(f'Call get_safety_stock_filter(): {start_date}, {end_date}')

    pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    print(len(pairs))

    all_options = [{'label': 'all', 'value': 'all'}]
    for wid, pid in pairs:
        all_options.append({'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'})
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


def get_safety_stock_figure(df, current_option, start_date, end_date):
    print(f'Call get_safety_stock_figure(): {current_option}, {start_date}, {end_date}')
 
    figure = None
    if current_option == 'all':
        df_group = (
            df.loc[
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
            .groupby('date')
            .sum()
            .reset_index()
        )
        print(f'df_group:\n{df_group.head()}')
        print(df_group.info())

        figure = plot_bar_chart(
            df_group,
            x='date',
            y='quantity',
            title=f'Safety stock for all products between {start_date} and {end_date}'
        )
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date),
                ['date', 'quantity']
            ]
        )
        print(f'df_sub:\n{df_sub.head()}')
        print(df_sub.info())

        figure = plot_bar_chart(
            df_sub,
            x='date',
            y='quantity',
            title=f'Safety stock for ({wid}, {pid}) between {start_date} and {end_date}'
        )

    return figure


def get_safety_stock_statistics(df, current_option, start_date, end_date):
    print(f'Call get_safety_stock_statistics(): {current_option}, {start_date}, {end_date}')

    layout = html.Div(

    )

    return layout


def get_safety_stock_table(df, current_option, start_date, end_date):
    print(f'Call get_safety_stock_table(): {current_option}, {start_date}, {end_date}')

    df_sub = None
    if current_option == 'all':
        df_sub = df.loc[
            (df['date']>=start_date)&
            (df['date']<=end_date)
        ]
    else:
        current_option = current_option.replace('(', '').replace(')', '')
        wid = int(current_option.split(',')[0]),
        pid = int(current_option.split(',')[0])
        print(f'selected (wid, pid)=({wid}, {pid})')

        df_sub = df.loc[
            (df['warehouse_id']==wid)&
            (df['product_id']==pid)&
            (df['date']>=start_date)&
            (df['date']<=end_date),
        ]

    table_layout = dash_table.DataTable(
        data=df_sub.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df_sub.columns],
        page_size=15
    )

    layout = html.Div(
        id = 'table-safety-stock',
        children=[table_layout],
    )

    return layout


def get_safety_stock_layout(df, current_option, start_date, end_date):
    print(f'Call get_safety_stock_layout(): {current_option}, {start_date}, {end_date}')

    filters = get_safety_stock_filter(df, start_date, end_date)
    figure = get_safety_stock_figure(df, current_option, start_date, end_date)
    statistics = get_safety_stock_statistics(df, current_option, start_date, end_date)
    # table = get_safety_stock_table(df, current_option, start_date, end_date)

    return filters, figure, statistics


