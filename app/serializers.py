#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

import json

from .encoders import AlchemyEncoder


def to_dict(obj):
    return json.loads(json.dumps(obj, cls=AlchemyEncoder))
