import pytest
from pyramid import testing


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from app import create_app

    app = create_app()
    from webtest import TestApp

    return TestApp(app)


def test_layout_root(testapp):
    """Test the contents of the home"""
    response = testapp.get("/", status=200)
    html = response.html
    assert "Welcome to Chinook Database Viewer" in html.text


def test_customer_layout(testapp):
    """Test the contents of the customer page"""
    response = testapp.get("/db/Chinook/Customer.html", status=200)
    html = response.html
    assert "This is Customer table from Chinook Database" in html.text


def test_employee_layout(testapp):
    """Test the contents of the employee page"""
    response = testapp.get("/db/Chinook/Employee.html", status=200)
    html = response.html
    assert "This is Employee table from Chinook Database" in html.text


def test_customer_filter_layout(testapp):
    """Test the contents of the customer filer page"""
    response = testapp.get("/db/Chinook/Customer/State/ON.html", status=200)
    html = response.html
    tables = html.findChildren('table')
    customer_table = tables[0]
    rows = customer_table.findChildren(['tr'])
    assert len(rows) == 3


def test_employee_filter_layout(testapp):
    """Test the contents of the employee filter page"""
    response = testapp.get("/db/Chinook/Employee/City/Calgary.html", status=200)
    html = response.html
    tables = html.findChildren('table')
    customer_table = tables[0]
    rows = customer_table.findChildren(['tr'])
    assert len(rows) == 6
