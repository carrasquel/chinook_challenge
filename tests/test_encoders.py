import json

from app.dao import CustomerDAO
from app.encoders import AlchemyEncoder


def test_alchemy_encoder():
    expected = '{"Address": "Pra\\u00e7a Pio X, 119", "City": "Rio de Janeiro", "Company": "Riotur", "Country": "Brazil", "CustomerId": 12, "Email": "roberto.almeida@riotur.gov.br", "Fax": "+55 (21) 2271-7070", "FirstName": "Roberto", "LastName": "Almeida", "Phone": "+55 (21) 2271-7000", "PostalCode": "20040-020", "State": "RJ", "SupportRepId": 3, "by_module": null, "classes": null, "employee": null, "invoice_collection": null, "prepare": null, "registry": null}'

    customer = CustomerDAO.read(12)
    res = json.dumps(customer, cls=AlchemyEncoder)

    assert res == expected
