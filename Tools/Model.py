#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np


class Model:
    def __init__(self, reverseIndex):
        self.reverseIndex = reverseIndex
        self.cos_lengths = None
        self.y = None

    def fit(self, X, y):
        self.calc_cos_lengths(X)
        self.y = y

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