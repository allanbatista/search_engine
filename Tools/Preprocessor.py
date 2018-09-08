#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re


class Preprocessor:
    def __init__(self, stemmer=True, min_word_size=2, stopwords=nltk.corpus.stopwords.words("english")):
        self.stemmer = stemmer
        self.min_word_size = min_word_size
        self.stopwords = stopwords
        self.porter_stemmer = nltk.PorterStemmer()

    def fits(self, texts):
        return [self.fit(text) for text in texts]

    def fit(self, text):
        words = self._tokenize(text)
        words = self._remove_stopwords(words)
        words = self._stemmer(words)

        return words

    def _tokenize(self, text):
        return [word for word in re.split('[\W\d]+', text.lower()) if len(word) > self.min_word_size]

    def _remove_stopwords(self, words):
        return [word for word in words if word not in self.stopwords]

    def _stemmer(self, words):
        return [str(self.porter_stemmer.stem(word)) for word in words]