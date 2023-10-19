from app.dao import CustomerDAO, EmployeeDAO


class TestCustomerDAO:
    def test_read_all_customers(self):
        customers = CustomerDAO.read_all()

        assert len(customers) == 59

    def test_read_customer(self):
        customer = CustomerDAO.read(17)

        assert customer.FirstName == "Jack"
        assert customer.LastName == "Smith"
        assert customer.Email == "jacksmith@microsoft.com"

    def test_filter_by_customer(self):
        customers = CustomerDAO.filter_by("Country", "USA")

        assert len(customers) == 13


class TestEmployeeDAO:
    def test_read_all_employee(self):
        employee = EmployeeDAO.read_all()

        assert len(employee) == 8

    def test_read_employee(self):
        employee = EmployeeDAO.read(5)

        assert employee.FirstName == "Steve"
        assert employee.LastName == "Johnson"
        assert employee.Email == "steve@chinookcorp.com"

    def test_filter_by_employee(self):
        employee = EmployeeDAO.filter_by("City", "Calgary")

        assert len(employee) == 5
