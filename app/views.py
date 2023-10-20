#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyramid.view import view_config

from .dao import CustomerDAO, EmployeeDAO


@view_config(renderer="app:templates/home.mako", route_name="home")
def home(request):
    return {}


@view_config(renderer="app:templates/table.mako", route_name="customer")
def customer_view(request):
    res = CustomerDAO.read_all()
    res = [CustomerDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": None,
        "value": None,
        "table": "Customer",
    }


@view_config(renderer="app:templates/table.mako", route_name="customer_filter")
def customer_filter_view(request):
    filter_column = request.matchdict["column"]
    filter_value = request.matchdict["value"]

    res = CustomerDAO.filter_by(filter_column, filter_value)
    res = [CustomerDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": filter_column,
        "value": filter_value,
        "table": "Customer",
    }


@view_config(renderer="app:templates/table.mako", route_name="employee")
def employee_view(request):
    res = EmployeeDAO.read_all()
    res = [EmployeeDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": None,
        "value": None,
        "table": "Employee",
    }


@view_config(renderer="app:templates/table.mako", route_name="employee_filter")
def employee_filter_view(request):
    filter_column = request.matchdict["column"]
    filter_value = request.matchdict["value"]

    res = EmployeeDAO.filter_by(filter_column, filter_value)
    res = [EmployeeDAO.to_dict(item) for item in res]
    headers = []

    if res:
        headers = list(res[0].keys())

    return {
        "rows": res,
        "headers": headers,
        "column": filter_column,
        "value": filter_value,
        "table": "Employee",
    }
