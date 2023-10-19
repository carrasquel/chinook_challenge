#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.database import session, Customer
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
        "Email"
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
