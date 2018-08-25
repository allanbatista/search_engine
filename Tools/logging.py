from config import CONFIG

import logging

logger = logging.FileHandler(CONFIG['logpath'])
logger.setLevel(getattr(logging, CONFIG['loglevel']))

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.info('creating an instance of auxiliary_module.Auxiliary')