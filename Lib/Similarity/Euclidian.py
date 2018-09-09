#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from Lib.Similarity.Similarity import Similarity

class Euclidian(Similarity):

    def predict(self, doc):
        results = []

        for index in range(self.total):
            x = self.X[index]

            sum = 0.0

            for pi, qi in zip(x, doc):
                sum += math.pow(pi - qi, 2)

            results.append([self.y[index], math.sqrt(sum)])

        results.sort(reverse=True, key=lambda x: x[1])

        return results

