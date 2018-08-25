#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Config import CONFIG
from Tools.Logger import logger
from Tools.Document import Document
from Tools.Preprocessing import Preprocessing
from Tools.ReverseIndex import ReverseIndex
from Tools.VectorizeTFIDF import VectorizeTFIDF

logger.info('Starting Application')

documents = Document.parse_many(CONFIG['documents'])
documents['pre'] = Preprocessing(**CONFIG['preprocessing']).preprocessing_many(documents['text'])

reverseIndex = ReverseIndex()
reverseIndex.create(documents)
reverseIndex.persist(CONFIG['reverse_index']['filename'])

vectorize = VectorizeTFIDF(reverseIndex, len(documents))
documents['vectorize'] = vectorize.vectorize(documents['pre'])
print(documents['vectorize'])