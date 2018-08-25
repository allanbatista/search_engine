#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Logger import logger
import json

class ReverseIndex:
    def __init__(self):
        self.index = {}
        self.count_documents_in_word = {}
        self.words = []

    def create(self, X, y):
        self.index = {}

        for index in len(X):
            for token in X[index]:
                try:
                    self.index[token].append(y[index])
                except:
                    self.index[token] = [y[index]]

        self.load_envs()

        return self.index

    def load_envs(self):
        self.words = sorted(list(set(self.index.keys())))

        for key in self.words:
            self.count_documents_in_word[key] = len(set(self.index[key]))

    def persist(self, filename):
        with open(filename, 'w+') as f:
            f.write(self.index_to_str())

    def index_to_str(self):
        lines = ["{};{}".format(key, json.dumps(self.index[key])) for key in self.index.keys()]
        return "\n".join(lines)