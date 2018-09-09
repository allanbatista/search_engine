#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import json

from Tools.Logger import logger
from Tools.ReverseIndex import ReverseIndex


class Model:
    def __init__(self, reverse_index=None):
        self.reverseIndex = reverse_index
        self.cos_lengths = None
        self.y = None
        self.X = None

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.cos_lengths = self.calc_cos_lengths(X)

        return self

    def persist(self, filename):
        self.reverseIndex.persist("{}.cos.reverse_index.csv".format(filename))

        with open("{}.cos.lengths.json".format(filename), 'w+') as f:
            f.write(json.dumps(self.cos_lengths))

        with open("{}.cos.y.json".format(filename), 'w+') as f:
            f.write(json.dumps(self.y.tolist()))

        with open("{}.cos.X.json".format(filename), 'w+') as f:
            f.write(json.dumps(self.X.tolist()))

    def load(self, filename):
        self.reverseIndex = ReverseIndex.load("{}.cos.reverse_index.csv".format(filename))

        with open("{}.cos.lengths.json".format(filename), 'r') as f:
            self.cos_lengths = json.loads(f.read())

        with open("{}.cos.y.json".format(filename), 'r') as f:
            self.y = np.array(json.loads(f.read()))

        with open("{}.cos.X.json".format(filename), 'r') as f:
            self.X = np.array(json.loads(f.read()))

        logger.info("Model Loaded")

    def calc_cos_lengths(self, X):
        return [self.calc_cos_length(x) for x in X]

    def calc_cos_length(self, doc):
        summed = sum([math.pow(weight, 2) for weight in doc])
        return math.sqrt(summed)

    def predict(self, doc):
        doc_length = self.calc_cos_length(doc)

        div = [cos_length * doc_length for cos_length in self.cos_lengths]

        mult = self.X * doc

        summeds = [sum(line) for line in mult]

        results = [[self.y[index], summeds[index] / div[index]] for index in range(len(summeds))]
        results.sort(reverse=True, key=lambda x: x[1])

        return [r for r in results]