#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""
from pyramid.view import view_config

from .dao import CustomerDAO, EmployeeDAO


@view_config(renderer="app:templates/home.mako", route_name="home")
def home(request):
    return {}


@view_config(renderer="app:templates/table.mako", route_name="customer")
def customer_view(request):
    limit = request.params.get("limit")
    filter_column = request.params.get("filterColumn")
    filter_value = request.params.get("filterValue")

    if filter_column and filter_value:
        res = CustomerDAO.filter_by(filter_column, filter_value)
    else:
        res = CustomerDAO.read_all(limit)

    res = [CustomerDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": filter_column,
        "value": filter_value,
        "table": "Customer"
    }


@view_config(renderer="app:templates/table.mako", route_name="employee")
def employee_view(request):
    limit = request.params.get("limit")
    filter_column = request.params.get("filterColumn")
    filter_value = request.params.get("filterValue")

    if filter_column and filter_value:
        res = EmployeeDAO.filter_by(filter_column, filter_value)
    else:
        res = EmployeeDAO.read_all(limit)

    res = [EmployeeDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": filter_column,
        "value": filter_value,
        "table": "Employee"
    }
