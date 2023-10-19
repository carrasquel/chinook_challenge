#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from .encoders import AlchemyEncoder


def to_dict(obj):
    return json.loads(json.dumps(obj, cls=AlchemyEncoder))
