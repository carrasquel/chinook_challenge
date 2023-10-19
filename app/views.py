#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from pyramid.response import Response
from pyramid.view import view_config

from .database import session, Album
from .serializers import to_dict


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
    limit = request.params['limit']
    filter_column = request.params['filterColumn']
    filter_value = request.params['filterValue']

    if limit:
        limit = int(limit)
        res = session.query(Album).limit(limit).all()
    else:
        res = session.query(Album).limit(20).all()
    
    res = [to_dict(item) for item in res]
    header = res[0].keys()

    return {'rows': res, 'header': header}


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
