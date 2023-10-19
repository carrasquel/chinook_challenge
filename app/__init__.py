#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""
from pyramid.config import Configurator

from .views import *
from .database import *


def create_app():

    with Configurator() as config:
        config.add_route('home', '/')
        config.scan('app.views')
        app = config.make_wsgi_app()

    return app