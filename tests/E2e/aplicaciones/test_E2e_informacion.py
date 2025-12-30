import pytest
pytestmark = pytest.mark.no_db
@pytest.mark.e2e

def test_informacion_page(page, live_server):
    page.goto(live_server.url + "/informacion/")

    assert "Información" in page.content()
