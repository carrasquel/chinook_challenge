#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid.config import Configurator

from .database import *
from .views import *


def create_app():
    with Configurator() as config:
        config.add_route("home", "/")
        config.add_route("customer", "/db/Chinook/Customer.html")
        config.add_route("customer_filter", "/db/Chinook/Customer/{column}/{value}.html")
        config.add_route("employee", "/db/Chinook/Employee.html")
        config.add_route("employee_filter", "/db/Chinook/Employee/{column}/{value}.html")
        config.scan("app.views")
        config.include("pyramid_mako")
        app = config.make_wsgi_app()

    return app
