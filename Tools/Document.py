#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from Tools.Logger import logger
import pandas as pd


class Document:

    @classmethod
    def load_documents(cls, filename):
        return pd.read_csv(filename)

    @classmethod
    def parse_many(cls, filenames):
        results = []

        for rs in [cls.parse(filename) for filename in filenames]:
            results += rs

        logger.info("{} Total Documents in {} files".format(len(results), len(filenames)))
        return pd.DataFrame(results, columns=['id', 'text'])

    @classmethod
    def parse(cls, filename):
        logger.info("Started Parse {}".format(filename))
        records = []

        for record in parse(filename).documentElement.getElementsByTagName("RECORD"):
            id = record.getElementsByTagName('RECORDNUM')[0].childNodes[0].data.strip()
            text = None

            try:
                text = record.getElementsByTagName('ABSTRACT')[0].childNodes[0].data
            except IndexError:
                try:
                    text = record.getElementsByTagName('EXTRACT')[0].childNodes[0].data
                except IndexError:
                    logger.warning("Document[" + id + "] doesn't have abstract neither extract!")

            if id and text:
                records.append([id, text.strip()])
                logger.info('Document[{}] added'.format(id))
            else:
                logger.warning('Document[{}] skipped because has no abstract or extract'.format(id))

        logger.info("{} documents parsed in {}".format(len(records), filename))
        return records
