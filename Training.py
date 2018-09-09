#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Config import CONFIG, ROOT_DIR
from Tools.Logger import logger
from Tools.Document import Document
from Tools.Preprocessor import Preprocessor
from Tools.ReverseIndex import ReverseIndex
from Tools.VectorizeTFIDF import vectorize
from Tools.ModelCos import Model

logger.info('Starting Training')

documents = Document.parse_many(CONFIG['documents'])
logger.info("Parsed Documents")
documents['pre'] = Preprocessor(**CONFIG['preprocessing']).fits(documents['text'])
logger.info("Created Normalized Documents")
reverseIndex = ReverseIndex().create(documents['pre'].values, documents['id'].values)
logger.info("Created Reverse Index")
documents['vectorize'] = vectorize(reverseIndex, documents['pre'])
logger.info("Create Vectorize")
documents.to_json(ROOT_DIR + "/" + CONFIG['documents_path'], orient='records')

model = Model(reverseIndex).fit(documents['vectorize'], documents['id'])
logger.info("Trained Model")
model.persist(ROOT_DIR + "/" + CONFIG['models_path'])
logger.info("Persisted Model")