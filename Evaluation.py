#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Config import CONFIG, ROOT_DIR
from Tools.Logger import logger
from Tools.ModelCos import Model
from Tools.EvaluatorData import EvaluatorData
from Tools.Preprocessor import Preprocessor
from Tools.VectorizeTFIDF import vectorize
import pandas as pd

logger.info('Starting Application')

model = Model()
model.load(ROOT_DIR + "/" + CONFIG['models_path'])

evaluator_data = EvaluatorData(ROOT_DIR + "/Data/cfquery.xml")

preprocessor = Preprocessor()

# results = []
#
# for query in evaluator_data.queries[0:5]:
#     print("Predicting {}".format(query['result']))
#     doc = preprocessor.fit(query['query_text'])
#     vec = vectorize(model.reverseIndex, [doc])[0]
#     p_ids, p_scores = [], []
#
#     for result in model.predict(vec):
#         p_ids.append(result[0])
#         p_scores.append(result[1])
#
#     mean = sum(p_scores) / len(p_ids)
#
#     data = {
#         'mean': mean,
#         'total': len(p_ids),
#         'scores': p_scores,
#         'p_ids': p_ids,
#         'tp': query['result'] in p_ids,
#         'fp': query['result'] not in p_ids
#     }
#
#     results.append(data)
#
# results = pd.DataFrame(results)

# Precision
#
# precision = results['tp'].sum() / ( results['tp'].sum() + results['fp'].sum() )
# print(precision)
# # recall = results.sum('tp') / ( results.sum('tp') + results.sum('fp'))

