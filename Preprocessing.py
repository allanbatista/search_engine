#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Config import CONFIG
from Tools.Logger import logger
from Tools.Document import Document
from Lib.NLP.Preprocessor import Preprocessor
from Lib.ReverseIndex import ReverseIndex
from Lib.NLP.VectorizeTFIDF import vectorize

logger.info('Starting Preprocessing')

document = Document.parse_many(CONFIG['documents'])
document.samples['pre'] = Preprocessor(**CONFIG['preprocessing']).fits(document.samples['text'])

logger.info("Creating ReverseIndex")
reverse_index = ReverseIndex().create(document.samples['pre'].values, document.samples['id'].values)
reverse_index.persist()
logger.info("Created ReverseIndex")

logger.info("Start Vectorize Samples")
document.samples['vectorize'] = vectorize(reverse_index, document.samples['pre'])
logger.info("Finish Vectorize Samples")

document.persit()
logger.info("Persisted Samples")

logger.info('Finish Preprocessing')