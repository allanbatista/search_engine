#!/usr/bin/env python
# -*- coding: utf-8 -*

import math

class VectorizeTFIDF:
    def __init__(self, reverseIndex, total):
        self.reverseIndex = reverseIndex
        self.total = total

    def vectorize(self, docs_tokens):
        return [self.terms_to_dev(terms) for terms in docs_tokens]

    def _tf(self, term, terms):
        return terms.count(term) / float(len(terms))

    def _idf(self, term):
        return math.log(self.total / self.reverseIndex.count_documents_in_word[term])

    def _tfidf(self, term, terms):
        return self._tf(term, terms) * self._idf(term)

    def terms_to_dev(self, terms):
        return [self._tfidf(word, terms) for word in self.reverseIndex.words]