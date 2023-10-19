#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from pyramid.response import Response
from pyramid.view import view_config


@view_config(
    route_name='home'
)
def home(request):
    return Response('Welcome!')


@view_config(
    renderer='app:templates/base.mak',
    route_name='album'
)
def album_view(request):
    return {'a':'1'}


@view_config(
    renderer='app:templates/table.mak',
    route_name='artist'
)
def artist_view(request):
    return {'a':'1'}


@view_config(
    renderer='app:templates/base.mak',
    route_name='customer'
)
def customer_view(request):
    return {'a':'1'}
