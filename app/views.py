#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from pyramid.response import Response
from pyramid.view import view_config

from .dao import CustomerDAO


@view_config(
    route_name='home'
)
def home(request):
    return Response('Welcome!')


@view_config(
    renderer='app:templates/table.mako',
    route_name='customer'
)
def customer_view(request):
    limit = request.params.get("limit")
    filter_column = request.params.get("filterColumn")
    filter_value = request.params.get("filterValue")

    if filter_column and filter_value:
        res = CustomerDAO.filter_by(filter_column, filter_value)
    else:
        res = CustomerDAO.read_all(limit)
    
    res = [CustomerDAO.to_dict(item) for item in res]
    headers = list(res[0].keys())

    return {"rows": res, "headers": headers}
