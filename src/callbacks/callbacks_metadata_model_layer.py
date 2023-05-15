import json
from dash import html, dcc, callback, Input, Output, State
from src.callbacks.callbacks_common import logger, dict_dh_objects
from src.layouts.layouts_model_layer import get_inventory_layout, get_orders_layout, get_deliveries_layout, get_purchases_layout, get_procurements_layout, get_lead_time_layout, get_stock_outs_layout
from src.utils.cloud_setting import get_DataHandler_object
from src.utils.load_data import load_data


##################################################
#
# callback functions for metadata_model_layer
#
##################################################


@callback(
    Output(component_id='metadata-model-layer-filters', component_property='children'),
    Output(component_id='metadata-model-layer-figure', component_property='figure'),
    Output(component_id='metadata-model-layer-statistics', component_property='children'),
    # Output(component_id='metadata-model-layer-table', component_property='children'),
    Input(component_id='tabs-model-layer', component_property='value'),
    State(component_id='store-cloud-setting', component_property='data'),
)
def click_tabs_model_layer(tab_value, cloud_setting):
    logger.info(f'Call click_tabs_model_layer(): argument_1={tab_value}, argument_2={cloud_setting}')

    cloud_setting = json.loads(cloud_setting)
    logger.info(f'\tConvert {cloud_setting} into type={type(cloud_setting)}')
    
    dh_object = get_DataHandler_object(
        dict_dh_objects=dict_dh_objects,
        cloud_service=cloud_setting['cloud_service'],
        project=cloud_setting['project'],
        bucket=cloud_setting['bucket'],
        customer_name=cloud_setting['customer_name'],
    )

    start_date='2021-06-01'
    end_date='2021-12-31'

    path = f'customers/{cloud_setting["customer_name"]}/model/'

    '''
    dcc.Store() has size limit upto 10 MB
    Becayse our dataframes are about 100 MB, we have to save to local.
    '''

    if tab_value == 'tab_model_layer_inventory':
        df_inventory = load_data(
            dh_object=dh_object,
            path=path,
            table_name='inventory_levels'
        )
        print(f'df_inventory:\n{df_inventory.head()}')
        print(df_inventory.info())

        return get_inventory_layout(
            df=df_inventory,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_demands':
        df_mdo = load_data(
            dh_object=dh_object,
            path=path,
            table_name='monthly_demand_from_orders'
        )
        df_mdd = load_data(
            dh_object=dh_object,
            path=path,
            table_name='monthly_demand_from_deliveries'
        )
        df_ddo = load_data(
            dh_object=dh_object,
            path=path,
            table_name='daily_demand_from_orders'
        )
        df_ddd = load_data(
            dh_object=dh_object,
            path=path,
            table_name='daily_demand_from_deliveries'
        )

        print(f'df_mdo:\n{df_mdo.head()}')
        print(df_mdo.info())
        print(f'df_mdd:\n{df_mdd.head()}')
        print(df_mdd.info())
        print(f'df_ddo:\n{df_ddo.head()}')
        print(df_ddo.info())
        print(f'df_ddd:\n{df_ddd.head()}')
        print(df_ddd.info())

        dict_df_demands = {
            'mdo': df_mdo,
            'mdd': df_mdd,
            'ddo': df_ddo,
            'ddd': df_ddd,
        }

        return get_demands_layout(
            df=dict_df_demands,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_orders':
        df_orders = load_data(
            dh_object=dh_object,
            path=path,
            table_name='orders'
        )
        print(f'df_orders:\n{df_orders.head()}')
        print(df_orders.info())

        return get_orders_layout(
            df=df_orders,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_deliveries':
        df_deliveries = load_data(
            dh_object=dh_object,
            path=path,
            table_name='deliveries'
        )
        print(f'df_deliveries:\n{df_deliveries.head()}')
        print(df_deliveries.info())

        return get_deliveries_layout(
            df=df_deliveries,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_purchases':
        df_purchases = load_data(
            dh_object=dh_object,
            path=path,
            table_name='purchases'
        )
        print(f'df_purchases:\n{df_purchases.head()}')
        print(df_purchases.info())

        return get_purchases_layout(
            df=df_purchases,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_procurements':
        df_procurements = load_data(
            dh_object=dh_object,
            path=path,
            table_name='procurements'
        )
        print(f'df_procurements:\n{df_procurements.head()}')
        print(df_procurements.info())

        return get_procurements_layout(
            df=df_procurements,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_lead_time':
        df_lead_time = load_data(
            dh_object=dh_object,
            path=path,
            table_name='lead_time'
        )
        print(f'df_lead_time:\n{df_lead_time.head()}')
        print(df_lead_time.info())

        return get_lead_time_layout(
            df=df_lead_time,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_stock_outs':
        df_stock_outs = load_data(
            dh_object=dh_object,
            path=path,
            table_name='stock_outs'
        )
        print(f'df_stock_outs:\n{df_stock_outs.head()}')
        print(df_stock_outs.info())

        return get_stock_outs_layout(
            df=df_stock_outs,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )

    elif tab_value == 'tab_model_layer_safety_stock':
        df_safety_stock = load_data(
            dh_object=dh_object,
            path=path,
            table_name='safety_stock'
        )
        print(f'df_safety_stock:\n{df_safety_stock.head()}')
        print(df_safety_stock.info())

        return get_safety_stock_layout(
            df=df_safety_stock,
            current_option='all',
            start_date=start_date,
            end_date=end_date
        )



@callback(
    Output(component_id='figure-model-layer-inventory', component_property='children'),
    Input(component_id='dropdown-pair', component_property='value'),
    Input(component_id='date-picker-range', component_property='start_date'),
    Input(component_id='date-picker-range', component_property='end_date'),
)
def update_figure_model_layer_inventory(selected_pair, start_date, end_date):
    logger.info(f'Call update_figure_model_layer_inventory(): {selected_pair}, {start_date}, {end_date}')


    if selected_pair == 'all':
        df_group = (
            df.loc[:, ['date', 'quantity']]
            .groupby('date')
            .sum()
            .reset_index()
            .rename(columns={'quantity': 'inventory'})
        )

        figure = px.line(
            df_group,
            x='date',
            y='inventory',
            title=f'Inventory levels for all products between {start_date} and {end_date}'
        )

    else:
        wid = int(selected_pair.split(',')[0].replace('(', ''))
        pid = int(selected_pair.split(',')[1].replace(')', ''))

        df_filtered = (
            df.loc[
                (df['warehouse_id']==wid)&
                (df['product_id']==pid)&
                (df['date']>=start_date)&
                (df['date']<=end_date)
            ]
            .rename(columns={'quantity': 'inventory'})
        )

        figure = px.line(
            df_filtered,
            x='date',
            y='inventory',
            title=f'Inventory levels for ({wid}, {pid}) between {start_date} and {end_date}',
        )

    return figure

 