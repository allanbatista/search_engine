#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import json

from Tools.Logger import logger
from Lib.ReverseIndex import ReverseIndex
from Lib.Similarity.Similarity import Similarity


class Cosine(Similarity):
    def __init__(self, reverse_index=None):
        self.reverseIndex = reverse_index
        self.lengths = None
        self.y = None
        self.X = None

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.lengths = self.calc_cos_lengths(X)

        return self

    def persist(self):

        data = {
            'lengths': self.lengths,
            'y': self.y.tolist(),
            'X': self.X.tolist()
        }

        with open(self.__class__.filename(), 'w+') as f:
            f.write(json.dumps(data))

    @classmethod
    def load(cls):
        cosine = cls()
        cosine.reverseIndex = ReverseIndex.load()

        with open(cls.filename(), 'r') as f:
            data = json.loads(f.read())
            cosine.lengths = data['lengths']
            cosine.y = np.array(data['y'])
            cosine.X = np.array(data['X'])

        logger.info("Model Cosine Loaded")

        return cosine

    def calc_cos_lengths(self, X):
        return [self.calc_cos_length(x) for x in X]

    def calc_cos_length(self, doc):
        summed = sum([math.pow(weight, 2) for weight in doc])
        return math.sqrt(summed)

    def predict(self, doc):
        doc_length = self.calc_cos_length(doc)

        div = [cos_length * doc_length for cos_length in self.lengths]

        mult = self.X * doc

        summeds = [sum(line) for line in mult]

        results = [[self.y[index], summeds[index] / div[index]] for index in range(len(summeds))]
        results.sort(reverse=True, key=lambda x: x[1])

        return [r for r in results]