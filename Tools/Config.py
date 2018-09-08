#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
import sys

CONFIG = yaml.load(open("application.yml", "r"))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)