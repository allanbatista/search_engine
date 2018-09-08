#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tools.Logger import logger
import json


class ReverseIndex:
    def __init__(self):
        self.index = {}
        self.count_documents_in_word = {}
        self.words = []
        self.total = None

    def create(self, X, y):
        self.index = {}
        self.total = len(X)

        for index in range(len(X)):
            for token in X[index]:
                try:
                    self.index[token].append(y[index])
                except KeyError:
                    self.index[token] = [y[index]]

        self.load_envs()

        return self

    def load_envs(self):
        self.words = sorted(list(set(self.index.keys())))

        for key in self.words:
            self.count_documents_in_word[key] = len(set(self.index[key]))

    def persist(self, filename):
        with open(filename, 'w+') as f:
            f.write(self.index_to_str())

    @classmethod
    def load(cls, filename):
        logger.info("Loading Reverse Index: {}".format(filename))
        ri = cls()

        with open(filename, 'r') as f:
            data = json.loads(f.read())
            ri.index = data['index']
            ri.count_documents_in_word = data['count_documents_in_word']
            ri.words = data['words']
            ri.total = data['total']

        return ri

    def index_to_str(self):
        return json.dumps({
            'index': self.index,
            'count_documents_in_word': self.count_documents_in_word,
            'words': self.words,
            'total': self.total
        })