import os
import pandas as pd
from .get_logger import get_logger
from cloudio import CloudIO

class DataHandler:
    def __init__(self,
            cloud_service,
            project,
            bucket,
            customer_name
        ):
        self._client = CloudIO(
            cloud_service,
            project,
            bucket
        )

        self._customer_name = customer_name

        self._logger = get_logger(enable_log=True)

        self._logger.info('Instantiate DataHandler object...')
        self._logger.info(f'In DataHandler::__init__(): cloud_service={cloud_service}, project={project}, bucket={bucket}, customer_name={customer_name}')


    def load_data(self,
            path,
            list_of_tables
        ):
        '''
        Load data
        path: parent path
        list_of_tables: table to be loaded
        '''
        table_paths = [f'{path}{table}' for table in list_of_tables]

        dict_dfs = {}
        for table in list_of_tables:
            dataframe = self._client.get_df(f'{path}{table}')
            for col in dataframe.columns:
                if 'warehouse_id' in col or 'product_id' in col:
                    dataframe[col] = dataframe[col].astype(int)
                if 'date' in col:
                    dataframe[col] = pd.to_datetime(
                        dataframe[col],
                        infer_datetime_format=True
                    )
            dict_dfs[table] = dataframe

        return dict_dfs


    def load_data_parallel(self,
            path,
            list_of_tables
        ):
        '''
        Load data in parallel
        path: parent path
        list_of_tables: table to be loaded
        '''
        table_paths = [f'{path}{table}' for table in list_of_tables]

        datasets = self._client.load_parallel(
            table_paths,
            logger=None
        )

        # Unpack 'datasets'
        dict_dfs = {}
        for table, dataframe in zip(list_of_tables, datasets):
            for col in dataframe.columns:
                if 'warehouse_id' in col or 'product_id' in col:
                    dataframe[col] = dataframe[col].astype(int)
                if 'date' in col:
                    dataframe[col] = pd.to_datetime(
                        dataframe[col],
                        infer_datetime_format=True
                    )
            dict_dfs[table] = dataframe

        return dict_dfs


    def get_metadata(self,
            layer,
            parallel=False
        ):
        '''
        Get metadata from network analyzer layer or model layer
        '''
        # all_tables = client.list_dir('customers/ingress/model/')
        # print(all_tables)

        data_tables = [
            'inventory_levels',
            'monthly_demand_from_orders',
            'monthly_demand_from_deliveries',
            'daily_demand_from_orders',
            'daily_demand_from_deliveries',
            'orders',
            'deliveries',
            'purchases',
            'procurements',
            'lead_time',
            'stock_outs',
            'safety_stock',
        ]

        path = f'customers/{self._customer_name}/{layer}/'

        self._logger.info(f'In DataHandler::get_metadata(): Load data from {path}...')

        dict_df_metadata = None
        if parallel:
            # When I use parallel=True in inspector, I will get the following error
            # RuntimeError: There is no current event loop in thread
            dict_df_metadata = self.load_data_parallel(path, data_tables) 
        else:
            dict_df_metadata = self.load_data(path, data_tables)

        self._logger.info(f'In DataHandler::get_metadata(): Finish loading data...')

        return dict_df_metadata


    def get_apni_results(self,
            apni_results_path,
            parallel=False
        ):
        '''
        Get AP&I AI and TR results from the apni_results_path
        '''
        print(f'Loading data from {apni_results_path}...')

        data_tables = ['AI', 'TR']

        dict_df_apni = {}
        if parallel:
            dict_df_apni = self.load_data_parallel(
                apni_results_path,
                data_tables
            )
        else:
            dict_df_apni = self.load_data(
                apni_results_path,
                data_tables
            )

        print('Finish loading data...')

        return dict_df_apni


    def get_simulator_results(self,
            simulator_results_path,
            parallel=False
        ):
        '''
        Get the simulator AI and TR results from the simulator_results_path
        '''
        data_tables = [
            'apni_purchases',
            'daily_consumption',
            'daily_production',
            'deliveries',
            'inventory_levels',
            'lost_sales',
            'orders',
            'procurements',
            'production_orders',
            'purchases',
            'resource_usage',
            'sim_records',
        ]

        print(f'Loading data from {simulator_results_path}...')

        dict_df_simulator = {}

        ai_path = f'{simulator_results_path}AI/'
        dict_df_simulator['AI'] = self.load_data_parallel(ai_path, data_tables)

        tr_path = f'{simulator_results_path}TR/'
        # dict_df_simulator['TR'] = self.load_data(tr_path, data_tables.remove('lost_sales'))

        # Currently, no lost sales table in TR, so I remove it
        tr_table = data_tables[:]
        tr_table.remove('lost_sales')
        dict_df_simulator['TR'] = self.load_data_parallel(tr_path, tr_table)

        print('Finish loading data...')

        return dict_df_simulator


    # def get_all_wid_pid_pairs(self, df):
    #     all_pairs = list(set(zip(df['warehouse_id'], df['product_id'])))
    #     # print(len(all_pairs))
    #     # print(all_pairs)
    #     return all_pairs


    # def get_list_of_options(self, all_pairs):
    #     list_of_option_pairs = []
    #     for pair in all_pairs:
    #         label = f'({pair[0]}, {pair[1]})'
    #         list_of_option_pairs.append({'label': label, 'value': label})
    #     print(len(list_of_option_pairs))
    #     # print(list_of_option_pairs)
    #     return list_of_option_pairs


