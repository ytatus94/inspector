from .data_handler import DataHandler
from .get_logger import get_logger


logger = get_logger(enable_log=True)

'''
If I instantiate a CloudIO object inside callback function, then I will get "RuntimeError: There is no current event loop in thread".
However, I couldn't find a solution for this. The temporary solution is trying to create many DataHandler objects outside the thread.

Here are the error message when I instantiate the CloudIO inside callback function:

Traceback (most recent call last):
  File "/Users/ytshen/Desktop/seeloz_mbp/repos/inspector/sw_app.py", line 351, in update_data
    client = CloudIO(
  File "/Users/ytshen/Desktop/seeloz_mbp/repos/CloudIO/cloudio/cloudio.py", line 35, in __init__
    self.cloud_service = CloudIO_AZ(
  File "/Users/ytshen/Desktop/seeloz_mbp/repos/CloudIO/cloudio/cloudio_az.py", line 47, in __init__
    self.blob_service_client_async = BlobServiceClientAsync(
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/storage/blob/aio/_blob_service_client_async.py", line 124, in __init__
    super(BlobServiceClient, self).__init__(
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/storage/blob/_blob_service_client.py", line 138, in __init__
    super(BlobServiceClient, self).__init__(parsed_url, service='blob', credential=credential, **kwargs)
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/storage/blob/_shared/base_client.py", line 112, in __init__
    self._config, self._pipeline = self._create_pipeline(self.credential, storage_sdk=service, **kwargs)
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/storage/blob/_shared/base_client_async.py", line 72, in _create_pipeline
    self._credential_policy = AsyncStorageBearerTokenCredentialPolicy(credential)
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/storage/blob/_shared/policies_async.py", line 240, in __init__
    super(AsyncStorageBearerTokenCredentialPolicy, self).__init__(credential, STORAGE_OAUTH_SCOPE, **kwargs)
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/site-packages/azure/core/pipeline/policies/_authentication_async.py", line 34, in __init__
    self._lock = asyncio.Lock()
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/asyncio/locks.py", line 81, in __init__
    self._loop = events.get_event_loop()
  File "/usr/local/anaconda3/envs/ray/lib/python3.9/asyncio/events.py", line 642, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
RuntimeError: There is no current event loop in thread 'Thread-12'.
'''


def create_all_DataHandler_objects():
    '''
    Create dhobj for all possible cloud setting combinations
    '''
    logger.info(f'Call create_all_DataHandler_objects()')

    # List all possible combinations
    dict_dh_objects = {
        'azure': {
            'seelozdevelop': {
                'dev': {
                    'ides': None,
                    'unifi': None,
                    'ingress': None,
                    'pactiv': None,
                },
                'prod': {
                    'ides': None,
                    'unifi': None,
                    'ingress': None,
                    'pactiv': None,
                },
                'test': {
                    'ides': None,
                    'unifi': None,
                    'ingress': None,
                    'pactiv': None,
                },
            },
        },
        'gcp': {},
        's3': {}

    }
    ####################
    #
    # Azure
    #
    ####################
    # Ides
    dict_dh_objects['azure']['seelozdevelop']['dev']['ides'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ides-dev',
        'ides'
    )
    dict_dh_objects['azure']['seelozdevelop']['prod']['ides'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ides-prod',
        'ides'
    )
    dict_dh_objects['azure']['seelozdevelop']['test']['ides'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ides-test',
        'ides'
    )

    # Unifi: No prod and test
    dict_dh_objects['azure']['seelozdevelop']['dev']['unifi'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-unifi-dev',
        'unifi'
    )
    # dict_dh_objects['azure']['seelozdevelop']['prod']['unifi'] = DataHandler(
    #     'azure',
    #     'seelozdevelop',
    #     'seeloz-unifi-prod',
    #     'unifi'
    # )
    # dict_dh_objects['azure']['seelozdevelop']['test']['unifi'] = DataHandler(
    #     'azure',
    #     'seelozdevelop',
    #     'seeloz-unifi-test',
    #     'unifi'
    # )

    # Ingress
    dict_dh_objects['azure']['seelozdevelop']['dev']['ingress'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ingress-dev',
        'ingress'
    )
    dict_dh_objects['azure']['seelozdevelop']['prod']['ingress'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ingress-prod',
        'ingress'
    )
    dict_dh_objects['azure']['seelozdevelop']['test']['ingress'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-ingress-test',
        'ingress'
    )

    # Pactiv
    dict_dh_objects['azure']['seelozdevelop']['dev']['pactiv'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-pactiv-dev',
        'pactiv'
    )
    dict_dh_objects['azure']['seelozdevelop']['prod']['pactiv'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-pactiv-prod',
        'pactiv'
    )
    dict_dh_objects['azure']['seelozdevelop']['test']['pactiv'] = DataHandler(
        'azure',
        'seelozdevelop',
        'seeloz-pactiv-test',
        'pactiv'
    )

    ####################
    #
    # GCP
    #
    ####################
    #dict_dh_objects['gcp']['<project>']['<bucket>']['<customer>'] = DataHandler(
    #    'gcp',
    #    <project>,
    #    <bucket>,
    #    <customer>
    #)

    ####################
    #
    # AWS S3
    #
    ####################
    #dict_dh_objects['aws']['<project>']['<bucket>']['<customer>'] = DataHandler(
    #    's3',
    #    <project>,
    #    <bucket>,
    #    <customer>
    #)


    return dict_dh_objects


def get_DataHandler_object(
        dict_dh_objects,
        cloud_service,
        project,
        bucket,
        customer_name
    ):
    logger.info(f'Call get_DataHandler_object():, {cloud_service}, {project}, {bucket}, {customer_name}')

    dh_object = dict_dh_objects[cloud_service][project][bucket][customer_name]

    return dh_object


