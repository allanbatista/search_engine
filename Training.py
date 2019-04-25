#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Logger import logger
from Tools.Document import Document
from Lib.ReverseIndex import ReverseIndex
from Lib.Similarity.Cosine import Cosine
from Lib.Similarity.Jaccard import Jaccard
from Lib.Similarity.Euclidian import Euclidian


documents = Document.load()

logger.info("Training Cosine Model")
model = Cosine(ReverseIndex.load())
model.fit(documents.samples['vectorize'], documents.samples['id'])
model.persist()
logger.info("Persisted Cosine Model")

logger.info("Training Jaccard Model")
model = Jaccard()
model.fit(documents.samples['vectorize'], documents.samples['id'])
model.persist()
logger.info("Persisted Jaccard Model")

logger.info("Training Euclidian Model")
model = Euclidian()
model.fit(documents.samples['vectorize'], documents.samples['id'])
model.persist()
logger.info("Persisted Euclidian Model")