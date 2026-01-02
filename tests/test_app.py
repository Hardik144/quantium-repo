import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#app-header")


def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-line-chart")


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-picker")
