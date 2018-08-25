#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from Tools.Config import CONFIG

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("application")
logger.setLevel(getattr(logging, CONFIG['loglevel']))

if CONFIG.get('logpath'):
    logfile = logging.FileHandler(CONFIG['logpath'])
else:
    logfile = logging.StreamHandler()

logfile.setFormatter(formatter)

logger.addHandler(logfile)