from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

from cloudio import CloudIO

client = CloudIO('azure', 'seelozdevelop', 'seeloz-ingress-dev')
tables = client.list_dir('customers/ingress/simulator/simulation_v1/2021-10-17/AI/')
print(tables)


dict_dfs = {}
for table in tables:
    print(table)
    dict_dfs[table] = client.get_df(f'customers/ingress/simulator/simulation_v1/2021-10-17/AI/{table}/records.parquet')

pairs = list(set(zip(dict_dfs['sim_records']['warehouse_id'], dict_dfs['sim_records']['product_id'])))
# df = client.get_df('customers/ingress/simulator/simulation_v1/2021-10-17/AI/sim_records/records.parquet')
# print(df.head())
# print(df.columns)
# pairs = list(set(zip(df['warehouse_id'], df['product_id'])))

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Simulator Analysis'),
    dcc.Dropdown(
        id='dropdown-pairs',
        options=[{'label': f'({wid}, {pid})', 'value': f'({wid}, {pid})'} for wid, pid in pairs],
        value=f'({pairs[0]}, {pairs[1]})'
    ),
    html.H2('daily_production'),
    dcc.Graph(id='graph-daily_production'),
    html.H2('apni_purchases'),
    dcc.Graph(id='graph-apni_purchases'),
    html.H2('daily_consumption'),
    dcc.Graph(id='graph-daily_consumption'),
    html.H2('orders'),
    dcc.Graph(id='graph-orders'),
    html.H2('lost_sales'),
    dcc.Graph(id='graph-lost_sales'),
    html.H2('deliveries'),
    dcc.Graph(id='graph-deliveries'),
    html.H2('procurements'),
    dcc.Graph(id='graph-procurements'),
    html.H2('purchases'),
    dcc.Graph(id='graph-purchases'),
    html.H2('sim-records'),
    dcc.Graph(id='graph-sim-records'),
    html.H2('production_orders'),
    dcc.Graph(id='graph-production_orders'),
    html.H2('resource_usage'),
    dcc.Graph(id='graph-resource_usage'),
    html.H2('inventory_levels'),
    dcc.Graph(id='graph-inventory_levels'),
])



['daily_production', 'apni_purchases', 'daily_consumption', 'orders', 'lost_sales', 'deliveries', 'procurements', 'purchases', 'sim_records', 'production_orders', 'resource_usage', 'inventory_levels']

@app.callback(
    Output('graph-daily_production', 'figure'),
    Output('graph-apni_purchases', 'figure'),
    Output('graph-daily_consumption', 'figure'),
    Output('graph-orders', 'figure'),
    Output('graph-lost_sales', 'figure'),
    Output('graph-deliveries', 'figure'),
    Output('graph-procurements', 'figure'),
    Output('graph-purchases', 'figure'),
    Output('graph-sim-records', 'figure'),
    Output('graph-production_orders', 'figure'),
    Output('graph-resource_usage', 'figure'),
    Output('graph-inventory_levels', 'figure'),
    Input('dropdown-pairs', 'value')
)
def update_figure(pair):
    wid = int(pair.split(',')[0].replace('(', ''))
    pid = int(pair.split(',')[1].replace(')', ''))
    print(wid, pid)

    filtered_df_daily_production = dict_dfs['daily_production'][(dict_dfs['daily_production']['warehouse_id']==wid)&(dict_dfs['daily_production']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_apni_purchases = dict_dfs['apni_purchases'][(dict_dfs['apni_purchases']['warehouse_id']==wid)&(dict_dfs['apni_purchases']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_daily_consumption = dict_dfs['daily_consumption'][(dict_dfs['daily_consumption']['warehouse_id']==wid)&(dict_dfs['daily_consumption']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_orders = dict_dfs['orders'][(dict_dfs['orders']['warehouse_id']==wid)&(dict_dfs['orders']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_lost_sales = dict_dfs['lost_sales'][(dict_dfs['lost_sales']['warehouse_id']==wid)&(dict_dfs['lost_sales']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_deliveries = dict_dfs['deliveries'][(dict_dfs['deliveries']['warehouse_id']==wid)&(dict_dfs['deliveries']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_procurements = dict_dfs['procurements'][(dict_dfs['procurements']['warehouse_id']==wid)&(dict_dfs['procurements']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_purchases = dict_dfs['purchases'][(dict_dfs['purchases']['warehouse_id']==wid)&(dict_dfs['purchases']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_sim_records = dict_dfs['sim_records'][(dict_dfs['sim_records']['warehouse_id']==wid)&(dict_dfs['sim_records']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_production_orders = dict_dfs['production_orders'][(dict_dfs['production_orders']['warehouse_id']==wid)&(dict_dfs['production_orders']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_resource_usage = dict_dfs['resource_usage'][(dict_dfs['resource_usage']['warehouse_id']==wid)&(dict_dfs['resource_usage']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)

    filtered_df_inventory_levels = dict_dfs['inventory_levels'][(dict_dfs['inventory_levels']['warehouse_id']==wid)&(dict_dfs['inventory_levels']['product_id']==pid)]
    fig = px.line(filtered_df, x="date", y="inventory")
    fig.update_layout(transition_duration=500)


    return filtered_df_daily_production, filtered_df_apni_purchases, filtered_df_daily_consumption, filtered_df_orders, filtered_df_lost_sales, filtered_df_deliveries, filtered_df_procurements, filtered_df_purchases, filtered_df_sim_records, filtered_df_production_orders, filtered_df_resource_usage, filtered_df_inventory_levels

#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[(df.warehouse_id == 2401)&(df.product_id==3558226422)]

#     fig = px.line(filtered_df, x="date", y="inventory")

#     fig.update_layout(transition_duration=500)

#     return fig


if __name__ == '__main__':
    app.run_server(debug=True)
