#!/usr/bin/env python
# -*- coding: utf-8 -*

import math


class VectorizeTFIDF:
    def __init__(self, reverse_index):
        self.reverseIndex = reverse_index

    def vectorize(self, docs_tokens):
        return [self.terms_to_dev(terms) for terms in docs_tokens]

    @staticmethod
    def _tf(term, terms):
        return terms.count(term) / float(len(terms))

    def _idf(self, term):
        return math.log(self.reverseIndex.total / float(self.reverseIndex.count_documents_in_word[term]))

    def _tfidf(self, term, terms):
        return self._tf(term, terms) * self._idf(term)

    def terms_to_dev(self, terms):
        return [self._tfidf(word, terms) for word in self.reverseIndex.words]


def vectorize(reverse_index, docs_tokens):
    return VectorizeTFIDF(reverse_index).vectorize(docs_tokens)