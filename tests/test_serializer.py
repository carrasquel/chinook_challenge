from app.serializers import to_dict
from app.dao import CustomerDAO

def test_dict_serializer():

    expected = {'Address': 'Praça Pio X, 119', 'City': 'Rio de Janeiro', 'Company': 'Riotur', 'Country': 'Brazil', 'CustomerId': 12, 'Email': 'roberto.almeida@riotur.gov.br', 'Fax': '+55 (21) 2271-7070', 'FirstName': 'Roberto', 'LastName': 'Almeida', 'Phone': '+55 (21) 2271-7000', 'PostalCode': '20040-020', 'State': 'RJ', 'SupportRepId': 3, 'by_module': None, 'classes': None, 'employee': None, 'invoice_collection': None, 'prepare': None, 'registry': None}
    customer = CustomerDAO.read(12)
    res = to_dict(customer)

    assert res == expected
