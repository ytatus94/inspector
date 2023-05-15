import os
import pandas as pd
from .get_logger import get_logger


def load_data(
        dh_object,
        path,
        table_name,
        force_reload=False
    ):
    '''
    If the data can be found on local, then load the local file.
    Otherwise, load the remote file and save it into local.
    '''

    logger = get_logger(enable_log=True)

    df = None

    if 'network_analyzer' in path or 'model' in path:
        layer = path.split('/')[-2]
    elif 'apni' in path:
        layer = 'apni'
    elif 'simulation' in path:
        layer = 'simulation'

    # Network analyzer layer or model layer
    if os.path.isfile(f'temp/{layer}/df_{table_name}.parquet') and force_reload is False:
        logger.info(f'\tFind temp/{layer}/df_{table_name}.parquet on local, load from local...')
        df = pd.read_parquet(f'temp/{layer}/df_{table_name}.parquet')
    else:
        logger.info(f'\tLoad {path}{table_name}/ table from remote...')
        dict_dfs = dh_object.load_data(path, [table_name])
        logger.info(f'\tFinish loading {path}{table_name}/ table...')

        df = dict_dfs[table_name]

        # manipulate demand tables
        selected_cols = [
            'warehouse_id',
            'product_id',
            'date',
            'demand',
        ]
        if table_name == 'monthly_demand_from_orders':
            df = (
                df.groupby(['warehouse_id', 'product_id', 'year', 'month'])
                .sum()
                .reset_index()
                .drop(columns=['site_id'])
            )
            df['date'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
            df = df.loc[:, selected_cols]
        elif table_name == 'monthly_demand_from_deliveries':
            df = (
                df.groupby(['warehouse_id', 'product_id', 'year', 'month'])
                .sum()
                .reset_index()
            )
            df['date'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))
            df = df.loc[:, selected_cols]
        elif table_name == 'daily_demand_from_orders':
            df = (
                df.groupby(['warehouse_id', 'product_id', 'date'])
                .sum()
                .reset_index()
                .drop(columns=['site_id'])
            )
            df = df.loc[:, selected_cols]
        elif table_name == 'daily_demand_from_deliveries':
            df = df.loc[:, selected_cols]

        if not os.path.isdir(f'temp/{layer}/'):
            os.makedirs(f'temp/{layer}/')

        # Save the file into local
        df.to_parquet(f'temp/{layer}/df_{table_name}.parquet', compression='snappy')
        logger.info(f'\tDataframe is dumped into local_file_path=temp/{layer}/df_{table_name}.parquet.')

    return df


