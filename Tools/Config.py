#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from pathlib import Path

CONFIG = yaml.load(open("application.yml", "r"))
ROOT_DIR = str(Path(__file__).parent.parent)
