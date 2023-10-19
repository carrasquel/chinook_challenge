#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from app.database import Customer, Employee, session
from app.serializers import to_dict


class CustomerDAO:
    columns = [
        "CustomerId",
        "FirstName",
        "LastName",
        "Company",
        "Address",
        "City",
        "State",
        "Country",
        "PostalCode",
        "Phone",
        "Fax",
        "Email",
    ]

    @classmethod
    def read_all(cls, limit=None):
        if not limit:
            return session.query(Customer).all()

        return session.query(Customer).limit(limit).all()

    @classmethod
    def read(cls, customer_id):
        res = session.query(Customer).filter_by(CustomerId=customer_id).first()

        return res

    @classmethod
    def filter_by(cls, column, value, limit=20):
        query = getattr(Customer, column).like("%" + value + "%")
        res = session.query(Customer).filter(query).limit(limit).all()

        return res

    @classmethod
    def to_dict(cls, customer):
        res = {}
        customer = to_dict(customer)

        for column in CustomerDAO.columns:
            res[column] = customer[column]

        return res


class EmployeeDAO:
    columns = [
        "EmployeeId",
        "FirstName",
        "LastName",
        "Title",
        "BirthDate",
        "HireDate",
        "Address",
        "City",
        "State",
        "Country",
        "PostalCode",
        "Phone",
        "Fax",
        "Email",
    ]

    @classmethod
    def read_all(cls, limit=None):
        if not limit:
            return session.query(Employee).all()

        return session.query(Employee).limit(limit).all()

    @classmethod
    def read(cls, employee_id):
        res = session.query(Employee).filter_by(EmployeeId=employee_id).first()

        return res

    @classmethod
    def filter_by(cls, column, value, limit=20):
        query = getattr(Employee, column).like("%" + value + "%")
        res = session.query(Employee).filter(query).limit(limit).all()

        return res

    @classmethod
    def to_dict(cls, employee):
        res = {}
        employee = to_dict(employee)

        for column in EmployeeDAO.columns:
            res[column] = employee[column]

        return res
