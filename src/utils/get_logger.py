import coloredlogs
import logging
import os


def get_logger(enable_log=False, log_path=None):
    local_logger = None

    if enable_log:
        # Creating an object
        local_logger = logging.getLogger()

        # If log_path is specified, write to log file and stdout
        if log_path is not None:
            log_folder = '/'.join(log_path.split('/')[:-1])

            if not os.path.exists(log_folder):
                os.makedirs(log_folder)

            logging.basicConfig(
                level=logging.INFO,
                handlers=[
                    logging.FileHandler(log_path),
                    logging.StreamHandler(sys.stdout)
                ]
            )
        else:
            logging.basicConfig(level=logging.INFO)

        format = '[+] %(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s'
        os.environ['COLOREDLOGS_LOG_FORMAT'] = format
        coloredlogs.install(
            level='INFO',
            logger=local_logger,
            isatty=True
        )

    return local_logger


