#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
from Tools.Config import ROOT_DIR, CONFIG


class EvaluatorData:

    def __init__(self):
        self.filename = ROOT_DIR + "/" + CONFIG['evaluation_query_path']
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
