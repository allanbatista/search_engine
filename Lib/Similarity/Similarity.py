#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import numpy as np

from Tools.Config import ROOT_DIR, CONFIG
from Tools.Logger import logger


class Similarity:

    def __init__(self):
        self.y = None
        self.X = None
        self.total = None

    def fit(self, X, y):
        self.y = y
        self.X = X
        self.total = len(y)

    def persist(self):
        data = {
            'y': self.y.tolist(),
            'X': self.X.tolist(),
            'total': self.total
        }

        with open(self.__class__.filename(), 'w+') as f:
            f.write(json.dumps(data))

    @classmethod
    def load(cls):
        m = cls()

        with open(cls.filename(), 'r') as f:
            data = json.loads(f.read())
            m.y = np.array(data['y'])
            m.X = np.array(data['X'])
            m.total = np.array(data['total'])

        logger.info("Model {} Loaded".format(cls.__name__))

        return m

    @classmethod
    def filename(cls):
        return ROOT_DIR + "/" + CONFIG["model_path"].format(class_name=cls.__name__)