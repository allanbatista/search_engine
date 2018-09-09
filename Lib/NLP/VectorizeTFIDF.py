#!/usr/bin/env python
# -*- coding: utf-8 -*

import math
from Tools.Logger import logger


class VectorizeTFIDF:
    def __init__(self, reverse_index):
        self.reverseIndex = reverse_index

    def vectorize(self, docs_tokens):
        results = []
        total = len(docs_tokens)

        for index in range(total):
            results.append(self.terms_to_dev(docs_tokens[index]))
            logger.debug("vectorize document {}/{}".format(index, total))

        return results

    @staticmethod
    def _tf(term, terms):
        return terms.count(term) / float(len(terms))

    def _idf(self, term):
        return math.log(self.reverseIndex.total / float(self.reverseIndex.count_documents_in_word[term]))

    def _tfidf(self, term, terms):
        return self._tf(term, terms) * self._idf(term)

    def terms_to_dev(self, terms):
        results = []

        for word in self.reverseIndex.words:
            results.append(self._tfidf(word, terms))

        return results


def vectorize(reverse_index, docs_tokens):
    return VectorizeTFIDF(reverse_index).vectorize(docs_tokens)