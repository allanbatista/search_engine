#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import json

from Tools.ReverseIndex import ReverseIndex


class Model:
    def __init__(self):
        self.reverseIndex = ReverseIndex()
        self.cos_lengths = None
        self.y = None

    def fit(self, X, y):
        self.reverseIndex.create(X, y)
        self.calc_cos_lengths(X)
        self.y = y

    def persist(self, filename):
        self.reverseIndex.persist("{}.cos.reverse_index.csv".format(filename))

        with open("{}.cos.lengths.json".format(filename), 'w+') as f:
            f.write(json.dumps(self.cos_lengths.tolist()))

        with open("{}.cos.labels.json".format(filename), 'w+') as f:
            f.write(json.dumps(self.y.tolist()))

    def calc_cos_lengths(self, X):
        cos_lengths = []

        for index in range(len(X)):
            zeros = np.zeros(len(X[index]))
            zeros[index] = self.calc_cos_length(X[index])
            cos_lengths.append(zeros)

        self.cos_lengths = np.array(cos_lengths)

    def calc_cos_length(self, doc):
        summed = sum([weight * weight for weight in doc])
        length = math.sqrt(summed)
        return length

    def predict(self, doc):
        doc_length = self.calc_cos_length(doc)

        div = [sum(cos_length) * doc_length for cos_length in self.cos_lengths]

        mult = self.cos_lengths * doc

        summeds = np.array([sum(line) for line in mult])

        results = [[self.y[index], summeds[index] / div[index]] for index in range(len(summeds))]
        results.sort(reverse=True, key=lambda x: x[1])

        return results