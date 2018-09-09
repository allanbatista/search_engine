#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from Tools.Logger import logger
import pandas as pd


class EvaluatorData:

    def __init__(self, filename):
        self.filename = filename
        self.queries = []
        self.parse_data()

    def parse_data(self):
        for record in parse(self.filename).documentElement.getElementsByTagName("QUERY"):
            self.queries.append({
                'query_number': record.getElementsByTagName('QueryNumber')[0].childNodes[0].data.strip(),
                'query_text': record.getElementsByTagName('QueryText')[0].childNodes[0].data.strip(),
                'result': record.getElementsByTagName('Results')[0].childNodes[0].data.strip(),
                'items': [n.childNodes[0].data.strip().zfill(5) for n in record.getElementsByTagName('Records')[0].getElementsByTagName('Item')]
            })
