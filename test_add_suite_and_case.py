from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_suite_add_case(app):
    app.open_home_page()
    app.login()
    app.create_suite()
    app.fill_suite_firm(suite_title="Test suite for M540_ATC_13292 IBP Diastolic low alarm limit")
    app.create_and_fill_case(case_title="M540_ATC_13292 Diastolic low alarm limit Adult mmHg")

