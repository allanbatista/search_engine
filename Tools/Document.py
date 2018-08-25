#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from Tools.Logger import logger
import pandas as pd


class Document:

    @classmethod
    def parse_many(cls, filenames):
        results = []

        for rs in [cls.parse(filename) for filename in filenames]:
            results += rs

        return pd.DataFrame(results, columns=['id', 'text'])

    @classmethod
    def parse(cls, filename):
        records = []

        for record in parse(filename).documentElement.getElementsByTagName("RECORD"):
            id = record.getElementsByTagName('RECORDNUM')[0].childNodes[0].data
            text = None

            try:
                text = record.getElementsByTagName('ABSTRACT')[0].childNodes[0].data
            except IndexError:
                try:
                    text = record.getElementsByTagName('EXTRACT')[0].childNodes[0].data
                except IndexError:
                    logger.warning("Document[" + id + "] doesn't have abstract neither extract!")

            if id and text:
                records.append([id.strip(), text.strip()])

        return records
