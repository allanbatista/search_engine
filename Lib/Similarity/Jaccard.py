#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import json

from Tools.Logger import logger
from Lib.Similarity.Similarity import Similarity


class Jaccard(Similarity):

    def predict(self, doc):
        results = []

        for index in range(self.total):
            x = self.X[index]

            sum_max = 0.0
            sum_min = 0.0

            for xi, yi in zip(x, doc):
                sum_min += min(xi, yi)
                sum_max += max(xi, yi)

            try:
                results.append([self.y[index], sum_min / sum_max])
            except ZeroDivisionError:
                results.append([self.y[index], 0.0])

        results.sort(reverse=True, key=lambda x: x[1])

        return results

