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
