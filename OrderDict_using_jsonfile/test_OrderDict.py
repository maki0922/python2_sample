#!/usr/bin/env python
# coding: UTF-8
import os
import sys
import json
from collections import OrderedDict
"""
Ref : https://stackoverflow.com/questions/6921699/can-i-get-json-to-load-into-an-ordereddict
重要: separatorsの2valueで「,」/ 「:」のseparatorの細かいところを制御する
"""
data = json.load(open('test.json'), object_pairs_hook=OrderedDict)
print json.dumps(data, indent=4, separators=(',', ': '))
