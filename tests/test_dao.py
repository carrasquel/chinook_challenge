from app.dao import CustomerDAO, EmployeeDAO


def test_read_all_customers():
    customers = CustomerDAO.read_all()
    
    assert len(customers) == 59


def test_read_customer():
    customer = CustomerDAO.read(17)

    assert customer.FirstName == "Jack"
    assert customer.LastName == "Smith"
    assert customer.Email == "jacksmith@microsoft.com"



def test_read_all_employee():

    employee = EmployeeDAO.read_all()

    assert len(employee) == 8